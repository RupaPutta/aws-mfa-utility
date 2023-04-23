# aws-mfa-utility

**Project Title:** To Manage AWS Multi-Factor Authentication Security Credentials

**Project Objective:** This project makes managing a user's AWS SDK Security Credentials easy when Multi-Factor Authentication (MFA) is enforced on the user's account. It automates the process of obtaining temporary credentials from the AWS Security Token Service and updating the user's AWS credentials file located at `~/.aws/credentials`.

**Inspired From:**  https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#alternatives-to-long-term-access-keys

_"In many scenarios, you don't need long-term access keys that never expire (as you have when you create access keys for an IAM user). Instead, you can create IAM roles and generate temporary security credentials. Temporary security credentials include an access key ID and a secret access key, but they also include a security token that indicates when the credentials expire. After they expire, they're no longer valid."_

**Project Status:** Active

**Tech Stack Required to build this project:**
* GitHub
* Python
* Microsoft Authenticator App
* Amazon Web Services Sign-In
* Amazon Resource Name (ARN, Ex: arn:aws:iam::196995266064:mfa/cs)
* Access key
* Secret access key

**Group Name:** Course Project Spring 2023

**Professor:**  Dr. Jun Wang

**Team Members:**
* Sri Sowmya Rupa Putta
* Bala Chandini Thanugundla
* Vishnu Priya Pati
* Angel Nakkala

**Video:**
[aws-mfa-utility-video.mp4](video%2Faws-mfa-utility-video.mp4)

**Installation:**
```text
git clone https://github.com/RupaPutta/aws-mfa-utility.git
python setup.py install
```

**Credentials File Setup:**

In a typical AWS credentials file (located at `~/.aws/credentials`), credentials are stored in sections, denoted by a pair of brackets: `[]`. The `[default]` section stores your default credentials. You can store multiple sets of credentials using different profile names. If no profile is specified, the `[default]` section is always used.

By default long term credential sections are identified by the convention `[<profile_name>-long-term]` and short term credentials are identified by the typical convention: `[<profile_name>]`. The following illustrates how you would configure you credentials file using **aws-mfa** with your default credentials:

```ini
[default-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY
```

After running `aws-mfa`, your credentials file would read:

```ini
[default-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY


[default]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>
```

Similarly, if you utilize a credentials profile named **development**, your credentials file would look like:

```ini
[development-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY
```


After running `aws-mfa`, your credentials file would read:

```ini
[development-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY

[development]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>
```

The default naming convention for the credential section can be overriden by using the `--long-term-suffix` and
`--short-term-suffix` command line arguments. For example, in a multi account scenario you can have one AWS account
that manages the IAM users for your organization and have other AWS accounts for development, staging and production
environments.

After running `aws-mfa` once for each environment with a different value for `--short-term-suffix`, your credentials
file would read:

```ini
[myorganization-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY

[myorganization-development]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>

[myorganization-staging]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>

[myorganization-production]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>
```

This allows you to access multiple environments without the need to run `aws-mfa` each time you want to switch
environments.

If you don't like the a long term suffix, you can omit it by passing the value `none` for the `--long-term-suffix`
command line argument. After running ``aws-mfa`` once for each environment with a different value for
`--short-term-suffix`, your credentials file would read:

```ini
[myorganization]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY

[myorganization-development]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>

[myorganization-staging]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>

[myorganization-production]
aws_access_key_id = <POPULATED_BY_AWS-MFA>
aws_secret_access_key = <POPULATED_BY_AWS-MFA>
aws_security_token = <POPULATED_BY_AWS-MFA>
```

**Usage:**

```
--device arn:aws:iam::123456788990:mfa/dudeman
                        The MFA Device ARN. This value can also be provided
                        via the environment variable 'MFA_DEVICE' or the
                        ~/.aws/credentials variable 'aws_mfa_device'.
--duration DURATION     The duration, in seconds, that the temporary
                        credentials should remain valid. Minimum value: 900
                        (15 minutes). Maximum: 129600 (36 hours). Defaults to
                        43200 (12 hours), or 3600 (one hour) when using
                        '--assume-role'. This value can also be provided via
                        the environment variable 'MFA_STS_DURATION'.
--profile PROFILE       If using profiles, specify the name here. The default
                        profile name is 'default'. The value can also be
                        provided via the environment variable 'AWS_PROFILE'.
--long-term-suffix LONG_TERM_SUFFIX
                        To identify the long term credential section by
                        [<profile_name>-LONG_TERM_SUFFIX]. Use 'none' to
                        identify the long term credential section by
                        [<profile_name>]. Omit to identify the long term 
                        credential section by [<profile_name>-long-term].
--short-term-suffix SHORT_TERM_SUFFIX
                        To identify the short term credential section by
                        [<profile_name>-SHORT_TERM_SUFFIX]. Omit or use 'none'
                        to identify the short term credential section by
                        [<profile_name>].
--assume-role arn:aws:iam::123456788990:role/RoleName
                        The ARN of the AWS IAM Role you would like to assume,
                        if specified. This value can also be provided via the
                        environment variable 'MFA_ASSUME_ROLE'
--role-session-name ROLE_SESSION_NAME
                        Friendly session name required when using --assume-
                        role. By default, this is your local username.
```

**Argument precedence**: Command line arguments take precedence over environment variables.

**Usage Example:**

Run **aws-mfa** *before* running any of your scripts that use any AWS SDK.


Using command line arguments:

```sh
$> aws-mfa --duration 1800 --device arn:aws:iam::196995266064:mfa/cs
INFO - Using profile: default
INFO - Your credentials have expired, renewing.
Enter AWS MFA code for device [arn:aws:iam::123456788990:mfa/dudeman] (renewing for 1800 seconds):123456
INFO - Success! Your credentials will expire in 1800 seconds at: 2015-12-21 23:07:09+00:00
```