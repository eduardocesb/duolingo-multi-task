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

This tool is intended for educational purposes only. Please respect Duolingo's terms of use. The creators of ***Duolingo Multi Task*** are not responsible for any actions taken by its users.

## Acknowledgements

- Duolingo for providing an excellent platform for language learning.
