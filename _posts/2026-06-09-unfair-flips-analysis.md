---
layout: post
title: "Unfair Flips: Optimal Strategy via Markov Chains and Dynamic Programming"
categories:
- Notes
- Algorithms
- Machine Learning
- Programming
- Probability
- AI Generated
date: 2026-06-09 00:00 +0000
---

[Unfair Flips](https://store.steampowered.com/app/2835570/Unfair_Flips/) is a Steam idle game where you flip coins to earn money,
then spend that money on upgrades that make you flip faster, earn more per flip, or increase your win probability.
I wanted to know: what's the mathematically optimal upgrade path?

This post is the story of that analysis — the dead ends, the model that finally worked, some surprising findings, and a real playthrough to verify.

## The Setup

The game has four upgradeable parameters:

- **Flip probability** `p`: chance of heads, starts at 20%, upgrades add 5pp each (8 levels, costs 1¢ → $100k)
- **Base worth** `b`: cents earned per head in a streak (4 levels: 1¢, 5¢, 10¢, 25¢, $1)
- **Combo multiplier** `m`: each consecutive head multiplies payout (5 levels: 1×→3.5×, costs 1¢→$100)
- **Flip duration** `d`: time per flip (5 levels: 2.0s→1.0s, costs 1¢→$10k)

The k-th consecutive head in a streak earns $$b \cdot \lceil m^{k-1} \rceil$$ cents.
At max multiplier (3.5×) the sequence per flip is 1¢, 4¢, 13¢, 43¢, 151¢, 526¢, $18.39, $64.34, $225.19, $788.16 — each flip worth exponentially more than the last.

The win condition: 10 consecutive heads. You accumulate cash from failed streaks and spend it on upgrades.

## Dead End: Greedy on Marginal Rate of Return

My first instinct was to greedily pick whichever upgrade maximises $$\Delta(\text{earnings/second}) / \text{cost}$$.
The problem: it's myopic. Buying a cheap low-value upgrade can prevent you from saving for a more transformative one sooner. The greedy path kept oscillating between small upgrades instead of building toward a big one.

## Dead End: Raw Flip Count

The next attempt tried to minimise total flip count. This ignored flip duration entirely — a 0.5s flip and a 2s flip both count as "one flip" but take very different wall-clock time. Any model that doesn't account for flip duration is measuring the wrong thing.

## What Actually Works: Markov Chain + DP

The correct model treats the game as a Markov chain over streak states \\(\\{0, 1, \ldots, 9\\}\\).

**Expected earnings per flip** in steady state is derived by summing over all streak outcomes:

$$E[\text{¢/flip}] = \frac{\sum_{k=0}^{9} p^k(1-p) \sum_{j=1}^{k} b\lceil m^{j-1}\rceil + p^{10} \sum_{j=1}^{10} b\lceil m^{j-1}\rceil}{\sum_{k=0}^{9} p^k(1-p)(k+1) + 10p^{10}}$$

**Optimal path**: dynamic programming over the state space `(p_level, b_level, m_level, d_level)`. At each state, try every upgrade, compute transition cost (time to save for it) + DP-optimal from the next state, and take the minimum. Memoised with `lru_cache`.

## The Optimal Path

The time-optimal path (21 steps, ~26 minutes expected):

| Step | Upgrade | Cost | ¢/flip after | Cumulative time |
|------|---------|------|--------------|-----------------|
| 1 | FlipMultiplier +0.5 | 1¢ | 0.20 | 10s |
| 2 | HeadsChance +5% | 1¢ | 0.25 | 18s |
| 3 | FlipTime -0.2s | 1¢ | 0.33 | 24s |
| 4 | FlipBaseWorth ↑ | 25¢ | 0.33 | 2.6min |
| … | … | … | … | … |
| 13 | FlipMultiplier +0.5 | $10 | 35.24 | 6.8min |
| … | … | … | … | … |
| 21 | HeadsChance +5% | $10k | 89.69 | 11.3min |
| → | WIN (55% per flip) | — | — | **25.9min** |

**Flip duration upgrades dominate the early game.** Halving your flip time compounds across every subsequent upgrade purchase, making it the most leveraged early investment.

## The Spread: How Much Do Wrong Choices Cost?

At each step I computed the "spread" — the gap in expected total time between the best and worst available upgrades.

**Step 13 is the highest-stakes decision in the game.** At state `p=35%, b=25¢, m=2.5×, d=1.4s`, both FlipMultiplier ($10) and FlipBaseWorth ($10) cost the same, but:

| Choice | Extra expected time |
|---|---|
| FlipMultiplier (optimal) | +0 |
| FlipBaseWorth | +4.5 min |

Most other steps have spreads under 30 seconds. But several mid-game steps where base worth and multiplier compete have spreads of 2–4 minutes — the game's hidden asymmetry.

## Wait Time Variance: Why You Get Stuck

The expected wait time for each upgrade is just `cost / E[¢/flip]`. But the *actual* wait time has high variance — especially at expensive upgrades where your earnings rate is still modest.

| Step | Upgrade | E[wait] | P95 wait |
|------|---------|---------|---------|
| 4 | FlipBaseWorth ↑ (25¢) | 2.2 min | 3.6 min |
| 12 | FlipBaseWorth ↑ ($6.25) | 1.0 min | 7.1 min |
| 16 | FlipBaseWorth ↑ ($100) | 1.3 min | **12.3 min** |
| 21 | HeadsChance ($10k) | 1.9 min | 10.1 min |

Step 16 (the $100 FlipBaseWorth upgrade) has a P95 wait of **12.3 minutes** vs the 1.3-minute expectation — a **9× ratio**. This is the most variance-prone step in the game. If you felt stuck here, it was bad luck, not bad strategy.

## How Bad Can Wrong Ordering Be?

I computed three strategies:

| Strategy | Expected time | ×optimal |
|---|---|---|
| Optimal | 25.9 min | 1.0× |
| 2nd-worst (avoids single worst choice each step) | 1.5 h | **3.4×** |
| Worst (always picks worst available) | 11,358 h | 26,296× |

The worst strategy — maxing HeadsChance before having any earnings — takes over a year of continuous play in expectation. But even avoiding just the single worst choice each step (2nd-worst) leaves you at 3.4× the optimal time. The ordering matters enormously, and "not the worst" is very different from "close to optimal."

## A Real Playthrough

After computing the optimal path, I played through the game following it exactly. Results:

- **Actual flips**: 2,220
- **Expected flips**: ~1,400
- **Percentile**: approximately P70–P75

2,220 flips is realistic — the distribution has a long right tail, and finishing at the ~70th percentile just means the streak phase was unlucky (needing more attempts than average to land 10 consecutive heads at 55%). The upgrade phase itself was fast, consistent with the model.

The model correctly predicted the two "stuck" points: the $100 FlipBaseWorth upgrade (Step 16) and the $10k HeadsChance upgrade (Step 21) both took noticeably longer than their expected values — consistent with their high P95/P99 variance.

## Code

The model is pure Python with no external dependencies beyond the standard library.
Full source: [github.com/adityagupta1089/unfair-flips-analysis](https://github.com/adityagupta1089/unfair-flips-analysis)
