# SYN-BND-001 — synthetic additive envelope

This bound is freshly written for UNI-RP-001-S.
This package does not test any C2O clause.
SYN-BND-001 is not a restatement of any corpus clause.

Let a pair of scalars (u, v) evolve together with a comparison scalar z.
The comparison map is psi(u, v) = (3u + v) / 4.
The error at step n is e_n = |psi(u_n, v_n) - z_n|.
The drive at step n (n >= 1) is d_n = |e_n - e_{n-1}|; d_0 = 0.

Declared parameters: a drive cap Delta >= 0, a working box W = [w_lo, w_hi],
and an ambient box B = [b_lo, b_hi] that contains W.

Premise. Each of u_n, v_n, and z_n lies in W, and d_n <= Delta.
Claim. e_n <= n * Delta.

The claim is an additive envelope. It is not a geometric series, and it has no
finite cap that stays valid for every duration.
