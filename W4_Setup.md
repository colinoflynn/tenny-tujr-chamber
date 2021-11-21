## Setup

The general setup is described in Section 7.3 of the user manual, which mentions `Digital Out 8` triggers the compressor and output `1A` triggers the heater. Note that there will be zero or more "Event Outputs" depending on your chambers. Ours had a N2 purge option and a LN2 fast cool-down option.

Those are triggered by some of the 'event outputs', you'll see a sticker on the back of your unit listing those events if you have them.

The following details what the settings were on our Watlow F4 controller for reference.

### Diagnostics Page

```
Model F4

Software #0
Revision 22.00

In 1: Univ Single
Out 1A: DC
Out 1B: DC
In1 AtoD: 6B14 (display showed 17C)
CJC1 AtoD 3569
CJC1 Temp 67.0F
```

### System

`System -> GSB 1 Source: Input 1 -> Guar. Soak Band 1: 1.0C -> [set date/time/units] -> Ch 1 Autotune SP: 90% -> Input 1 Fail: 0% -> Open Loop CH1: Off -> Power-Out Time: 10 sec -> Power Out Action: Continue`

`Digital Out 1 -> Event` (label on back details Event 1 usage if wired)

`Digital Out 2 -> Event` (label on back details Event 2 usage if wired)

`Digital Out 3 -> Off`

`Digital Out 4 -> Off`

`Digital Out 5 -> Off`

`Digital Out 6 -> Off`

`Digital Out 7 -> Off`

`Digital Out 8 -> Compressor -> Comp. on power: -20% -> Comp off power: 95% -> Comp off delay: 10 sec -> Comp on delay: 30 sec`

`Analog Input 1 -> RTD -> 100 ohm DIM -> Decimal: "0.0" -> SP Low Limit: -75C -> SP High Limit: 20C -> Cal Offset: -0.5C -> Filter Time: 1s -> Error-Latch: Self-Clear`

`Control Output 1A -> Function: Heat -> Cycle Time: Fixed Time -> Cycle Time: 5.0 sec -> Hi Power Limit: 100% -> Lo Power Limit: 0%`

`Control Output 1B -> Function: Cool -> Cycle Time: Fixed Time -> Cycle Time: 7.0 sec -> Hi Power Limit: 100% -> Lo Power Limit: 0%`

NOTE: This unit seems to not have anything connected to output 1B. Not sure if this is for other options or just unused setting.

`Alarm Output 1 -> Off`
`Alarm Output 2 -> Off`
`Digital Input N -> Off` (not used)

### PID

```
PID Set Channel 1 -> Set 1 -> "Prop Band1: 6C"
					 Set 2 -> "Prop Band1: 14C"
					 Set 3 -> "Prop Band1: 14C"
					 Set 4 -> "Prop Band1: 14C"
					 Set 5 -> "Prop Band1: 14C"
```