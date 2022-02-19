import argparse

import h5py

from dlgo import agent
from dlgo import httpfrontend


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind-address', default='127.0.0.1')
    parser.add_argument('--port', '-p', type=int, default=5000)
    parser.add_argument('--predict-agent')


    args = parser.parse_args()

    bots = {}

    if args.predict_agent:
        bots['predict'] = agent.load_prediction_agent(
            h5py.File(args.predict_agent))

    web_app = httpfrontend.get_web_app(bots)
    web_app.run(host=args.bind_address, port=args.port)


if __name__ == '__main__':
    main()
