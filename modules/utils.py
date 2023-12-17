import os
import time
import openai


openai.api_type = "azure"
# This version for openai.Completion
# openai.api_version = "2022-12-01"
# This version for openai.ChatCompletion.create()
openai.api_version = "2023-03-15-preview"
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")


def call_openai(
        messages: list,
        temperature: float = 0.7,
        max_tokens: int = 200
) -> str:
    while True:
        try:

            response = openai.ChatCompletion.create(
                engine="azure-openai-test-demo-002",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )

            return response['choices'][0].message.content.strip()

        except openai.error.RateLimitError:
            print(
                "   *** The OpenAI API rate limit has been exceeded. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        except openai.error.Timeout:
            print(
                "   *** OpenAI API timeout occurred. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        except openai.error.APIError:
            print(
                "   *** OpenAI API error occurred. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        except openai.error.APIConnectionError:
            print(
                "   *** OpenAI API connection error occurred. Check your network settings, proxy configuration, "
                "SSL certificates, or firewall rules. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        except openai.error.InvalidRequestError:
            print(
                "   *** OpenAI API invalid request. Check the documentation for the specific API method you are calling"
                ""
                " and make sure you are sending valid and complete parameters. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        except openai.error.ServiceUnavailableError:
            print(
                "   *** OpenAI API service unavailable. Waiting 10 seconds and trying again. ***"
            )
            time.sleep(10)  # Wait 10 seconds and try again
        else:
            break


if __name__ == "__main__":
    result = call_openai(prompt="Tell me a joke about cookies")
    print(result)