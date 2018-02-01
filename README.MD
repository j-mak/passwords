# Password module

Simple password module. It consist from simple password generator and simple strength meter.

### Install
1. `git clone https://github.com/j-mak/passwords.git`
2. `python3 setup.py develop`

#### Generator example
```python
python3 examples/example_generator.py                     
c$3WJ3x&M_a9
```

#### Strength meter example
```python
python3 examples/example_strange_meter.py 
Password: ''
Score: 0%
Result: Weak password
Visual: [          ]
--------------------------------------------------------------------------------
Password: 'aaaaaaaa'
Score: 8%
Result: Weak password
Visual: [#         ]
--------------------------------------------------------------------------------
Password: 'abcdefgh'
Score: 8%
Result: Weak password
Visual: [#         ]
--------------------------------------------------------------------------------
Password: '12345678'
Score: 8%
Result: Weak password
Visual: [#         ]
--------------------------------------------------------------------------------
Password: 'HaX0r666'
Score: 59.0%
Result: Medium password
Visual: [######    ]
--------------------------------------------------------------------------------
Password: 'ja-Skapem3!'
Score: 76.45%
Result: Strong password
Visual: [########  ]
--------------------------------------------------------------------------------
Password: '4%DHTMxYyyOc@F3p'
Score: 82.25%
Result: Strong password
Visual: [########  ]
--------------------------------------------------------------------------------
Password: '@d8l*7kUH5VtIt@V41v5NairgnOA#kKN'
Score: 94.75%
Result: Strong password
Visual: [######### ]
--------------------------------------------------------------------------------
Password: '@d8l*7kUH5VtIt@V41v5NairbceFGgnOA#KN'
Score: 96.11%
Result: Strong password
Visual: [##########]
```

### Warning!
Do not use for real applications, module was coded only for fun.

#### Author:
Jozef '**sunny**' Mak - <sunny@jozefmak.eu>