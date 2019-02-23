# import modules used here -- sys is a very standard one
import sys
from utils import *
from decimal import Decimal

# Gather our code in a main() function
def main():
    value = Decimal(sys.argv[1]) if len(sys.argv) > 1 else 0
    date_str = Decimal(sys.argv[2]) if len(sys.argv) > 2 else None

    print('Hello there ')

    rate = get_date_exchange_rate(date_str=date_str)

    print("""
      The rate for {date} is {rate}.
      USD {value} = C$ {total_nio}
      C$ {value} = USD {total_usd}
    """.format(
      value=value,
      rate=rate["value"],
      date=rate["date"],
      total_nio=value * rate["value"],
      total_usd= (value / rate["value"]).quantize(Decimal("0.0001")) if rate["value"] > 0 else 0
    ))
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
