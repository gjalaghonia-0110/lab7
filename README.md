# week 7 lab

## how to run

```bash
python3 part1_zkp.py
python3 part2_original.py
python3 part2_manual_obfuscated.py
python3 part2_auto_obfuscated.py
```

## part 1 - zkp

ali baba cave simulation. honest prover wins 100%, attacker has to guess (50% each round). over 20 rounds thats (1/2)^20 = basically 0 chance to fake it

## part 2 - obfuscation

what i did for manual obfuscation:
- renamed vars to random hex stuff like _0xDEAD
- replaced 0 with (lambda: 0)() and 1 with (True and 1)
- strings are chr() arrays now
- removed comments

auto obfuscation (simulated pyarmor style):
- base64 encoded stuff
- exec/eval
- bitwise ops like (5<<1) instead of 10

why? makes code annoying to read. not secure tho, just annoying

