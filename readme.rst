HotWallet Automation Bot
========================

.. image:: https://static.herewallet.app/intro.35bf1b5e.png
   :alt: HotWallet Automation Bot
   :width: 200
   :align: center

Automate your interactions with the HotWallet web application using this Python script powered by Selenium.

Key Features
------------

- **Telegram Login:** New version coming with telegram login.
- **Initial Login:** Handles login and navigates through the initial steps.
- **Periodic Check:** Periodically checks if the condition "Full" appears on a specific page. Then claim it, waits for 8 hours before checking again.
- **Automated Claim:** Performs a series of automated clicks on specific elements based on predefined XPaths.
- ~~Multi-Wallet Support~~: ~~Supports multiple wallets by reading seeds from separate `seed.txt`, and so on. Prompts user input if the file is empty.~~ (Patched By DEV)

How To Use
-----------

1. **Install Python**

If you don't have Python installed on your Windows machine, follow these steps:

   - **Download Python Installer:** Visit the `official Python website <https://www.python.org/downloads/release>`_ and download the latest version of Python for Windows.
   - **Run Python Installer:** Run the downloaded installer. Make sure to check the box that says "Add Python to PATH" during the installation process. Click "Install Now" to start the installation.
   - **Verify Installation:** Open a new command prompt or PowerShell window. Type the following command and press Enter::

       ```bash
       python --version
       ```

2. **Setup Bot**

.. code-block:: bash

   # Clone this repository
   $ git clone https://github.com/vannszs/HotWalletBot/

   # Go into the repository
   $ cd HotWalletBot

   # Install dependencies
   $ pip install selenium

   # Run the script
   $ python your_script.py

> **Note**
> If you're using Linux Bash for Windows, `see this guide <https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/>`_ or use ``node`` from the command prompt.

Download
----------

You can `download <https://github.com/vannszs/HotWalletBot/releases/>`_ the latest installable version of Markdownify for Windows, macOS, and Linux.

Credits
--------

This script uses the following open source packages:

- `Selenium <https://www.selenium.dev/>`_
- `Python <https://www.python.org/>`_

License
---------

MIT
