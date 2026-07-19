from magnesium.logging import *
from magnesium.handle import *
from magnesium.config import *

@safe
def main() -> None:
    log(getconf("welcome_message")).print()
    
main()