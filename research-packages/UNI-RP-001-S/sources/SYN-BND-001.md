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

Premise. For each k = 1,...,n, d_k = |e_k - e_{k-1}| <= Delta.
Claim. e_n <= e_0 + n * Delta.

Proof. By the triangle inequality,

    e_n <= e_{n-1} + |e_n - e_{n-1}| <= e_{n-1} + Delta.

Iterating gives e_n <= e_0 + n * Delta. The zero-initial-error form
(e_n <= n * Delta) is valid only when e_0 = 0; without that condition it is
false. For example, W = [0, 1], u = v = 1, z = 0, and Delta = 0 give
e_n = e_0 = 1 for a stationary sequence, while n * Delta = 0.

A separate box consequence follows because psi(u, v) = 3u/4 + v/4 is a
convex combination: if u_n, v_n, and z_n all remain in W, then psi(u_n,v_n)
and z_n lie in W, so e_n <= w_hi - w_lo. When both premises apply,

    e_n <= min(w_hi - w_lo, e_0 + n * Delta).

The additive envelope has no finite cap uniform over every duration unless
another bound (such as the working-box width) is maintained.
