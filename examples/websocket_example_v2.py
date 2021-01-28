import logging

from alpaca_trade_api.stream import Stream

log = logging.getLogger('')


async def print_trade(t):
    print('trade', t)


async def print_quote(q):
    print('quote', q)


async def print_trade_update(tu):
    print('trade update', tu)


def main():
    # TODO: better example
    logging.basicConfig(level=logging.INFO)
    stream = Stream(raw_data=True)
    # stream.subscribe_trade_updates(print_trade_update)
    stream.subscribe_trades(print_trade, '*')
    # stream.subscribe_quotes(print_quote, '*')

    @stream.on_bar('*')
    async def _(bar):
        print('bar', bar)

    stream.run()


if __name__ == "__main__":
    main()
