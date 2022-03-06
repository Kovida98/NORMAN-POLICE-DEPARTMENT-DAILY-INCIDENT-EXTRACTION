import argparse

import __init__

def main(url):
    # Download data
    incident_data = __init__.fetchincidents(url)

    # Extract data
    incidents = __init__.extractincidents(incident_data)

    # Create new database
    db = __init__.createdb()

    # Insert data
    __init__.populatedb(db, incidents)

    # Print incident counts
    __init__.status(db)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
