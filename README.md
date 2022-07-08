# horizon-as3
A template for F5 AS3 I've used to deploy vmware horizon for customers.

I've also included two python utilities for pushing/pulling from a BigIP, just as a reference.

do-do.py pushes the AS3
get-as3.py pulls down what was previously pushed, kind of a validation step.

Understand, manual configurations to the F5 will NOT be pulled down, only the rendered configuration from a previous push.
