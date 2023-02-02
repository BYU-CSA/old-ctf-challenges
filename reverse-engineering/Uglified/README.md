# Uglified

Category: Rev

Difficulty: Hard
# Prompt
Julian is learning JavaScript at school. His friend hid a flag inside some obfuscated JavaScript code; can you find help Julian find the flag and impress his friend?

# Solve

The initial Javascript is pretty ugly. However, if you put it into JS-Beautify on beautifier.io, it ends up looking like this:

```javascript
function _0x1aa9() {
    const _0x389ac8 = ['15474ppjiId', '112xWMqFK', '91944YYlzPP', '9549528saPKEm', '175130AEzihP', '1336010lgIsJU', 'length', '78rzleao', '2453RuSnkU', '56930JywvqQ', '3073GiLOLT', 'log', '2278674xSIeWT'];
    _0x1aa9 = function() {
        return _0x389ac8;
    };
    return _0x1aa9();
}
const _0x361ee1 = _0x448d;
(function(_0x4a2e51, _0x3bd8a6) {
    const _0x56342c = _0x448d,
        _0x5d6318 = _0x4a2e51();
    while (!![]) {
        try {
            const _0x3a02c6 = -parseInt(_0x56342c(0x172)) / 0x1 + parseInt(_0x56342c(0x167)) / 0x2 * (parseInt(_0x56342c(0x16f)) / 0x3) + parseInt(_0x56342c(0x16e)) / 0x4 * (-parseInt(_0x56342c(0x169)) / 0x5) + parseInt(_0x56342c(0x16d)) / 0x6 * (-parseInt(_0x56342c(0x16a)) / 0x7) + -parseInt(_0x56342c(0x170)) / 0x8 + -parseInt(_0x56342c(0x16c)) / 0x9 + -parseInt(_0x56342c(0x171)) / 0xa * (-parseInt(_0x56342c(0x168)) / 0xb);
            if (_0x3a02c6 === _0x3bd8a6) break;
            else _0x5d6318['push'](_0x5d6318['shift']());
        } catch (_0x224fc4) {
            _0x5d6318['push'](_0x5d6318['shift']());
        }
    }
}(_0x1aa9, 0xd39eb));

function _0x448d(_0x1d230a, _0xe0b8ca) {
    const _0x1aa939 = _0x1aa9();
    return _0x448d = function(_0x448df9, _0x545cdf) {
        _0x448df9 = _0x448df9 - 0x167;
        let _0x34a1b6 = _0x1aa939[_0x448df9];
        return _0x34a1b6;
    }, _0x448d(_0x1d230a, _0xe0b8ca);
}
const item = ['b', 'y', 'u', 'c', 't', 'z', 'f', '{', 'f', 'r', 'y', 'e', 's', 'd', 'g', 'p', 'l', 'a', 'g', '}'];
for (let i = 0x0; i < item[_0x361ee1(0x173)]; i++) {
    item[i] !== 'p' && i % 0x5 != 0x0 && console[_0x361ee1(0x16b)](item[i]);
}
```

Most of that is just to distract the user, but what we need is the last part:

~~~javascript
const item = ['b', 'y', 'u', 'c', 't', 'z', 'f', '{', 'f', 'r', 'y', 'e', 's', 'd', 'g', 'p', 'l', 'a', 'g', '}'];
for (let i = 0x0; i < item[_0x361ee1(0x173)]; i++) {
    item[i] !== 'p' && i % 0x5 != 0x0 && console[_0x361ee1(0x16b)](item[i]);
}
~~~

The loop will print out every character that is 1., not "p", and 2. not at an index that is an even multiple of 5. If you look at all the characters that meet those conditions, you'll get this flag:

byuctf{fresdglag}
