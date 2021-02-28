# How to set up the receipt printer

1. First use this repo to install CUPS drivers for the printer:

    ```shell
    git clone https://github.com/klirichek/zj-58.git

    cd zj-58

    mkdir build
    cd build

    cmake ..
    cmake --build .

    sudo make install
    ```

2. Now install the following programs to allow you to edit printer settings:

    ```shell
    sudo pacman -S system-config-printer cups
    ```
    or
    ```shell
    sudo apt install system-config-printer cups libcups2-dev
    ```

3. Now add the printer to your CUPS server and set up the proper settings

    ```shell
    sudo system-config-printer
    ```
    `Add` > `Unknown` > `Zijiang` > `ZJ-58` > `Apply`

    Right click the printer > `Properties` > `Printer Options` > `Media Size: 58mm x 210mm`

4. To print a file from the command line, use

    ```shell
    lp -d <printer name> <file>
    ```

*[Source](https://scruss.com/blog/2015/07/12/thermal-printer-driver-for-cups-linux-and-raspberry-pi-zj-58/)*
