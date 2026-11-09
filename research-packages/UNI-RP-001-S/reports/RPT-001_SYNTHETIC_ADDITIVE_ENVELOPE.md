# RPT-001 — synthetic additive envelope

This report summarizes UNI-RP-001-S. This package does not test any C2O clause.

Five authored cases were executed in exact rational arithmetic.

1. SIM-001. The still family kept error equal to zero for six samples, so the
   envelope held in a trivial way. This is a harness check, not a deep test.
2. SIM-002. The steady-drive family met the envelope with equality at every
   step: 0, 1/5, 2/5, 3/5, 4/5, 1. The additive form is sharp for that family.
3. SIM-003. The expanding family left the working box at step 1. The bound
   first failed at step 2, which is also when the state left the ambient box.
   A guarantee that is not re-checked after the working box is left is not a
   guarantee over the later steps.
4. SIM-004. The same sharp family shows the claimed bound growing with
   duration and crossing a reference budget of 1/2. The envelope has no
   finite uniform cap.
5. SIM-005. All 50 generated rows were reproduced with zero mismatches.

No owner credit is awarded. No independent review was performed. The package
is INTERNAL_CANDIDATE and is not release-authorized.
