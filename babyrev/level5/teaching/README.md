Firstly, you should create a file named `icsvb`.
The program skips 6 bytes.
The expected output is `76 73 6f 72 6c 61`, which interprets to `vsorla`.
We have to reverse the mangler so that we can get the input value for the answer.
Reversing it, it becomes `alrosv`.
Swapping the first and the fifth value, it becomes `slroav`.
Adding random 6 bytes, the answer becomes `aaaaaaslroav`.