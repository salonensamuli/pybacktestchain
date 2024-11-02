def test_new_blockchain():
    try:
        from pybacktestchain.data_module import FirstTwoMoments
        from pybacktestchain.broker import Backtest, StopLoss
        from pybacktestchain.blockchain import load_blockchain
        from datetime import datetime
        import random
        # Set verbosity for logging
        verbose = False  # Set to True to enable logging, or False to suppress it
        random_name = 'backtest' + str(random.randint(0, 1000))
        backtest = Backtest(
            initial_date=datetime(2019, 1, 1),
            final_date=datetime(2020, 1, 1),
            information_class=FirstTwoMoments,
            risk_model=StopLoss,
            name_blockchain=random_name,
            verbose=verbose
        )

        backtest.run_backtest()

        block_chain = load_blockchain(random_name)

        assert block_chain.is_valid(), 'Blockchain is not valid'
        # remove the blockchain pickle file
        block_chain.remove_blockchain(random_name)

    except Exception as e:
        assert False, e