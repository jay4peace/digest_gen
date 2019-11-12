import argparse
from hashlib import md5

def gen_digest(user, password, realm):
    return md5(':'.join((user, realm, password)).encode('utf-8')).hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Generating htdigest.')
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-r', '--realm', default='default')
    parser.add_argument('-f', '--form', default='htdigest',
        help='result print format(htdigest or tizen)')

    args = parser.parse_args()

    digest = gen_digest(args.user, args.password, args.realm)
    if args.form == "tizen":
        print('='.join((args.user, digest)))
    else :
        print(':'.join((args.user, args.realm, digest)))

if __name__=="__main__":
    main()
