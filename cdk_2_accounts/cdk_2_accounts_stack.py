from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct

class Cdk2AccountsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, env,prod_env, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        if prod_env:

            queue = sqs.Queue(
                self, "Cdk2AccountsQueue",
                visibility_timeout=Duration.seconds(300),
                queue_name="cdk2-accounts-queue-prod"+env.account
            )
            print("if :deploying into environment ", env)
            print("if :deploying into environment ", env.account)
            print("if :deploying into environment ", env.region)
        else:
            queue = sqs.Queue(
                self, "Cdk2AccountsQueue",
                visibility_timeout=Duration.seconds(300),
                queue_name="cdk2-accounts-queue-nonprod"+env.account
            )
            print("else :deploying into environment ",env)
            print("else :deploying into environment ", env.account)
            print("else :deploying into environment ", env.region)
            

