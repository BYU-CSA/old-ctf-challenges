# Buzz Off
* Level - Hard
* Author: Steve Palica

Description:
```
The bees! They're stealing my data! They must have flown in the window and hacked my computer! Luckily I have a handy packet capture. Now if only I could figure out how those dang bees stole my data, I could sue the bees! You believe me, right? I'm not going crazy, right?
```

## Writeup
Text is hidden in the TTL (Time to Live) value of the ICMP requests sent out by `10.37.216.141`. If you open the file in Wireshark and use the filter `ip.src == 10.37.216.141 && icmp.type != 11`, it will display 86,183 packets that contain the text. Using Python to script this and pull out the TTL value (convert to char from decimal code, `114` for TTL value is `'r'`) for packets matching this filter will give you a long text (the text of the Bee Movie??), with the flag hidden inside.

**Flag** - `byuctf{i_could_have_made_the_flag_much_longer_but_even_i_thought_that_would_bee_a_bit_much}`

