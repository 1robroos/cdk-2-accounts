#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_2_accounts.cdk_2_accounts_stack import Cdk2AccountsStack

# dev account:aws profile RobRoosDEV
dev = cdk.Environment(account='999592371459', region='us-east-1')

# DCT-PRODUCTION
prod = cdk.Environment(account='024530078564', region='us-east-1')

app = cdk.App()
Cdk2AccountsStack(app, "Cdk2AccountsStack-dev",env=dev,prod_env=False)
Cdk2AccountsStack(app, "Cdk2AccountsStack-prd",env=prod,prod_env=True)

app.synth()
