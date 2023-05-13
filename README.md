
# Certificate Generator

The certificate generator is a Python script that can be used to generate certificates for participants in events, conferences, and other occasions. The script supports a variety of font sizes and colors, and can be used to generate certificates in a variety of formats, including PDF, PNG, and JPEG. The script is easy to use, and can be installed with a single command.

The certificate generator is a useful tool for anyone who needs to generate certificates on a regular basis. It is also a great way to save time and effort, as it eliminates the need to manually create certificates.

## Features

The certificate generator has the following features:

-   Can generate certificates for participants in events, conferences, and other occasions.
-   Supports a variety of font sizes and colors.
-   Can be used to generate certificates in a variety of formats, including PDF, PNG, and JPEG.
- You can aslo use the .env file to edit you variables

## Requirements

To use the certificate generator, you will need to have the following installed:

-   Python 3.6 or later
-   pandas
-   PIL
-   dotenv

## Installation

To install the certificate generator, you can use the following command:

    clone this repository
    pip install -r requirements.txt
    
download your required fonts and place it into the fonts directory
## Usage
First upload the names of the students into the `participants.xlxs`
change your `.env` varibles as your requirement 

 1. Add the  Certficate path
 2. Adjust X_REDUCTION_FACTOR  and Y_REDUCTION_FACTOR
 3. Aet up you font size and colour

To use the certificate generator, you can use the following command:

    python run.py
The certificates will be saved in the `certificates` directory.

## License

The certificate generator is licensed under the MIT License.

## Contact

If you have any questions or feedback, please contact me at pavanvattikala.com
