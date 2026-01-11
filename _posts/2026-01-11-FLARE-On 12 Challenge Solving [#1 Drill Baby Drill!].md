---
title: FLARE-On 12 Challenge Solving [#1 Drill Baby Drill!]
date: 2026-01-11 14:37:29 +0900
categories: [Challenge, flare-on]
tags: [flare-on, flare-on-12, reverse-engineering, malware-analysis, xor, bruteforce]     # TAG names should always be lowercase
published: true
---

# Overview
The first FLARE-On 12 challenge, "Drill Baby Drill!", is a small pygame game. The binary implements the same logic used by the game to display the flag, which makes it a better target than reproducing gameplay. From a reverse engineering perspective, the fastest path is to bound the input domain for the flag generator and decode directly. The key point is that `GenerateFlagText` derives its key from game state (`bear_sum`).

```python
def GenerateFlagText(sum):
    # Flag is obfuscated with a linear XOR stream derived from sum.
    key = sum >> 8
    encoded = "\xd0\xc7\xdf\xdb\xd4\xd0\xd4\xdc\xe3\xdb\xd1\xcd\x9f\xb5\xa7\xa7\xa0\xac\xa3\xb4\x88\xaf\xa6\xaa\xbe\xa8\xe3\xa0\xbe\xff\xb1\xbc\xb9"
    plaintext = []
    for i in range(0, len(encoded)):
        plaintext.append(chr(ord(encoded[i]) ^ (key+i)))
    return ''.join(plaintext)
```

# Solving
The approach is straightforward. The key is computed as `sum >> 8`, so finding the maximum possible `sum` gives an upper bound for the key. With that bound, brute forcing the key space and filtering for printable ASCII yields a small set of viable candidates.

```python
if bear_mode:
    screen.blit(bearimage, (player.rect.x, screen_height - tile_size))
    if current_level == len(LevelNames) - 1 and not victory_mode:
        victory_mode = True
        # Flag generation is gated on the final level and bear state.
        flag_text = GenerateFlagText(bear_sum)
        print("Your Flag: " + flag_text)
```

# bear_sum
`bear_sum` is updated each time the player finds a bear. The update logic is concise and reveals the true input domain.

```python
if player.hitBear():
    player.drill.retract()
    # Multiplicative accumulator over player.x at each bear find.
    bear_sum *= player.x
    bear_mode = True
```

## bear_sum Calculation
### Initial value
`bear_sum` starts at 1.

### When a bear is found
Each bear multiplies `bear_sum` by the current player x coordinate (`player.x`).

### Bear location
Bears are found at `max_drill_level`, meaning the player must drill at a specific x coordinate to the maximum depth.

### player.x range
`player.x` moves within the horizontal tile count (`tiles_width`).  
`tiles_width = screen_width // tile_size`, which is `800 // 40 = 20` in this code.  
So `player.x` ranges from 0 to 19.

### Number of bears
There is one bear per level.  
The number of levels equals the length of `LevelNames`, which is 5 here.

### Maximum bear_sum
Each bear multiplies `bear_sum` by `player.x`.  
With a maximum `player.x` of 19 and 5 bears, the maximum is `19^5`.

Result: `19^5 = 2,476,099`.

# key
Apply an 8-bit right shift to the maximum `bear_sum` to obtain the key upper bound.

```bash
> 2476099 >> 8
9672
```

So brute forcing 0 to 9672 yields the candidate flags.

# brute force
The script below decodes across the key range and filters to printable ASCII.

```python
def GenerateFlagText(key):
    # key = sum >> 8 -> substitute the derived key directly
    encoded = "\xd0\xc7\xdf\xdb\xd4\xd0\xd4\xdc\xe3\xdb\xd1\xcd\x9f\xb5\xa7\xa7\xa0\xac\xa3\xb4\x88\xaf\xa6\xaa\xbe\xa8\xe3\xa0\xbe\xff\xb1\xbc\xb9"
    plaintext = []
    for i in range(0, len(encoded)):
        plaintext.append(chr(ord(encoded[i]) ^ (key+i)))
    return ''.join(plaintext)

def is_ascii(s):
    return all(32 <= ord(c) <= 126 for c in s)  # printable ASCII

unique_flags = set()  # dedupe candidates

for i in range(9672):
    flag = GenerateFlagText(i)
    if is_ascii(flag):  # keep only readable output
        unique_flags.add(flag)

# dump all candidates
print("\nUnique Flags:")
for flag in unique_flags:
    print(flag)
```

```bash
Unique Flags:
csjmchmfXgls ufechfrOgo`ud.nq/`nj
drilling_for_teddies@flare-on.com
```

# Result
Among the filtered outputs, the valid flag is `drilling_for_teddies@flare-on.com`. This result shows how constraining a state-derived key space can recover the flag without recreating gameplay.
