from gitsource import GithubRepositoryDataReader



def load_data():
    documents = []
    reader = GithubRepositoryDataReader(
        repo_owner="DataTalksClub",
        repo_name="llm-zoomcamp",
        commit_id="8c1834d",
        allowed_extensions={"md"},
        filename_filter=lambda path: "/lessons/" in path,
    )

    files = reader.read()

    for file in files:
        doc = file.parse()
        documents.append(doc)

    return documents