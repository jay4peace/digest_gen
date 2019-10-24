import argparse
from hashlib import md5

def gen_digest(user, password, realm):
    digest = md5(':'.join((user, realm, password)).encode('utf-8')).hexdigest()
    htdigest = ':'.join((user, realm, digest))
    print(htdigest)

def main():
    parser = argparse.ArgumentParser(description='Generating htdigest.')
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-r', '--realm', default='default')

    args = parser.parse_args()

    gen_digest(args.user, args.password, args.realm)

if __name__=="__main__":
    main()
