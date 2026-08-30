import hashlib
import urllib.request


def check_password_breach(password):

    # Create SHA-1 hash locally
    sha1_hash = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    # First 5 characters
    prefix = sha1_hash[:5]

    # Remaining characters
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Password-Strength-Analyzer"
            }
        )

        with urllib.request.urlopen(
            request,
            timeout=5
        ) as response:

            data = response.read().decode("utf-8")

        for line in data.splitlines():

            returned_suffix, count = line.split(":")

            if returned_suffix == suffix:

                return {
                    "compromised": True,
                    "count": int(count)
                }

        return {
            "compromised": False,
            "count": 0
        }

    except Exception as error:

        return {
            "compromised": None,
            "count": 0,
            "error": str(error)
        }

if __name__ == "__main__":

    password = input("Enter a password to check: ")

    result = check_password_breach(password)

    print(result)