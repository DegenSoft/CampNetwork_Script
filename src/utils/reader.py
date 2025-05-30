import json
from loguru import logger
from eth_account import Account
from eth_account.hdaccount import generate_mnemonic
from web3.auto import w3


def read_txt_file(file_name: str, file_path: str) -> list:
    with open(file_path, "r") as file:
        items = [line.strip() for line in file]

    logger.success(f"Successfully loaded {len(items)} {file_name}.")
    return items


def split_list(lst, chunk_size=90):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


def read_abi(path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


class InvalidKeyError(Exception):
    """Exception raised for invalid private keys or mnemonic phrases."""

    pass


def read_private_keys(file_path: str) -> list:
    """
    Read private keys or mnemonic phrases from a file and return a list of private keys.
    If a line contains a mnemonic phrase, it will be converted to a private key.

    Args:
        file_path (str): Path to the file containing private keys or mnemonic phrases

    Returns:
        list: List of private keys in hex format (with '0x' prefix)

    Raises:
        InvalidKeyError: If any key or mnemonic phrase in the file is invalid
    """
    private_keys = []

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, 1):
            key = line.strip()
            if not key:
                continue
            private_keys.append(key)
    logger.success(f"Successfully loaded {len(private_keys)} private keys.")
    return private_keys
