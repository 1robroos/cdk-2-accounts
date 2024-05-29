import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_2_accounts.cdk_2_accounts_stack import Cdk2AccountsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_2_accounts/cdk_2_accounts_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Cdk2AccountsStack(app, "cdk-2-accounts")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
