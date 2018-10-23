# Foo Bot

Class utility for [lunhg/WebWhatsapp-Wrapper](https://www.github.com/lunhg/WebWhatsapp-Wrapper)

# Download

```
$ git clone https://github.com/lunhg/WebWhatsapp-Wrapper-bot <path-to-clone>
```

# Usage

This repo is a implementation of [lunhg/WebWhatsapp-Wrapper-bot](https://www.github.com/lunhg/WebWhatsapp-Wrapper-bot).

You can clone this repo and customize, following the structure below:


```python
# Import os and check for SELENIUM* environment variables
import os
import sys

# Initialize foo bot
__foo__ = os.path.abspath('<path-to-bot-foo>')
sys.path.append(__foo__)
from foo import Foo

# Start Foo bot
f = Foo(client='firefox',
        botname='bot123',
        headless=True,
        plugins='<path-to-plugins>')
f.setup({
// TODO a conficuration following
// the name of added plugins
})
f.run()
```
