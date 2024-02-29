# Duolingo Multi Task

## Overview

***Duolingo Multi Task*** is a script designed to automate the process of completing lessons on Duolingo. With the capability to perform multiple lessons in parallel, users can earn XP quickly.

## Features

- **Automated Lesson Completion**: Automatically completes Duolingo lessons for you.
- **Parallel Tasking**: Capable of handling multiple lessons simultaneously, providing a swift XP gain.
- **Configurable**: Options to customize which lessons to take and how many instances to run in parallel.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- Required Python packages: all packages are listed in `requirements.txt` and can be installed using `pip`.

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:eduardocesb/duolingo-multi-task.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd duolingo-multi-task
    ```

3. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Rename `.env-example` to `.env` and edit it with your desired settings.
   1. `LESSON_URLS`: List of Duolingo lesson URLs to complete.
   2. `PROFILE_PATH`: Path to your Chrome profile.
   3. `SLEEP_TIME`: Time to wait between each lesson completion
   4. `NUMBER_OF_TABS`: Number of parallel tasks to run.

### Usage

To start earning XP automatically, simply run the script from the command line:

```bash
python main.py
```

## Contributing

Contributions to ***Duolingo Multi Task*** are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This tool, ***Duolingo Multi Task***, is developed for educational purposes and personal use only. It is designed to demonstrate the capabilities of automation and should be used responsibly and ethically with respect to Duolingo's terms of service and guidelines.

- **Compliance with Duolingo's Terms of Service**: Users are advised to review and comply with [Duolingo's Terms of Service](https://www.duolingo.com/terms) before using this tool. Any use of this script that violates Duolingo's terms is strictly prohibited and the responsibility of the user.

- **Fair Use Policy**: This script should be used in a way that does not harm Duolingo's service or other users' experience. It is not intended for cheating or gaining an unfair advantage in language learning progress.

- **Potential Risks**: Users should be aware that the use of automated scripts on Duolingo's platform may lead to account restrictions or bans if detected. The creators of ***Duolingo Multi Task*** will not be liable for any account issues, including restrictions or bans, resulting from the use of this script.

- **Educational Intent**: The primary intent of this tool is educational, to showcase programming and automation skills. It is not intended to encourage or promote any form of cheating or violation of service terms.

By using ***Duolingo Multi Task***, users acknowledge and agree to these terms, assuming full responsibility for any consequences that may arise from its use.

## Acknowledgements

- Duolingo for providing an excellent platform for language learning.
