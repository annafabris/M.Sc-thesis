import pandas as pd


def merge_arguments_and_key_points(arguments, key_points, labels):
    """
    Merge the arguments and key points in a single dataframe.

    Parameters:
    arguments (pandas.DataFrame): the arguments dataframe
    key_points (pandas.DataFrame): the key points dataframe
    labels (pandas.DataFrame): the labels dataframe

    Returns:
    pandas.DataFrame: the merged dataframe
    """
    df = key_points.merge(labels, on="key_point_id")
    df = arguments.merge(df, on=["arg_id", "stance", "topic"])
    #df.drop(columns=["arg_id", "key_point_id"], inplace=True)
    return df


def download_dataset_split(dataset_split):
    """
    Read the .csv dataset from its Github repository

    Parameters:
    dataset_split (str): the name of the dataset to split ['train', 'test', 'dev']

    Returns:
    pandas.DataFrame: the dataframe containing the dataset split

    """
    GITHUB_REPOSITORY_PATH = (
        "https://raw.githubusercontent.com/IBM/KPA_2021_shared_task/main/"
    )
    if dataset_split == "test":
        GITHUB_REPOSITORY_DIRECTORY = "test_data/"
    else:
        GITHUB_REPOSITORY_DIRECTORY = "kpm_data/"

    arguments = pd.read_csv(
        filepath_or_buffer=GITHUB_REPOSITORY_PATH
        + GITHUB_REPOSITORY_DIRECTORY
        + "arguments_"
        + dataset_split
        + ".csv"
    )
    key_points = pd.read_csv(
        filepath_or_buffer=GITHUB_REPOSITORY_PATH
        + GITHUB_REPOSITORY_DIRECTORY
        + "key_points_"
        + dataset_split
        + ".csv"
    )
    labels = pd.read_csv(
        filepath_or_buffer=GITHUB_REPOSITORY_PATH
        + GITHUB_REPOSITORY_DIRECTORY
        + "labels_"
        + dataset_split
        + ".csv"
    )
    return arguments, key_points, labels
