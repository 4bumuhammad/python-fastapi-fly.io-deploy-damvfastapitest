# Python fastapi fly.io deploy damvfastapitest


#### file structure :

    ❯ tree -L 2 -I 'gambar-petunjuk|README.md'

        ├── Dockerfile
        ├── fly.toml
        ├── main.py
        └── requirements.txt

        0 directories, 4 files


## Test application with Docker container

❯ docker build -t fastapitest . 
❯ docker run -d --name fastapitest-svc -p 10000:10000 fastapitest

### Open Browser

    http://localhost:10000

---

<p align="center">
    <img src="./gambar-petunjuk/fly-io-logo.svg" alt="fly-io-logo" style="display: block; margin: 0 auto;">
</p>

---

## Stages in deploying the application to fly.io


Reference : 

- commands flyctl agent `https://fly.io/docs/flyctl/agent/#main-content-start`

- manual pages `https://fig.io/manual/flyctl`


### create apps :

    ❯ flyctl apps create --name damvfastapitest

        Update available 0.0.456 -> v0.0.457.
        Run "flyctl version update" to upgrade.
        automatically selected personal organization: abumuhammad
        New app created: damvfastapitest


Attention!

if you get a flyctl version that is behind the current update, it's a good idea to update it. Otherwise when deploying flyctl, you will get the following error message: `Error failed to launch VM: flyctl version too old, must be at least 0.1.20`

    ❯ flyctl version

        Update available 0.0.456 -> v0.2.15.
        Run "flyctl version update" to upgrade.
        flyctl v0.0.456 darwin/arm64 Commit: 43371b58 BuildDate: 2023-02-08T22:32:29Z


update : 

    ❯ flyctl version update

        Update available 0.0.456 -> v0.2.11.
        Run "flyctl version update" to upgrade.
        /bin/zsh -c
        Running automatic update [curl -L "https://fly.io/install.sh" | sh]
        % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                        Dload  Upload   Total   Spent    Left  Speed
        100  1735    0  1735    0     0   2301      0 --:--:-- --:--:-- --:--:--  2313
        ######################################################################## 100.0%
        set update channel to shell
        flyctl was installed successfully to /Users/<user>/.fly/bin/flyctl
        Run 'flyctl --help' to get started


customize configuration with the fly.io installation installed `https://github.com/4bumuhammad/fly.io-install-on-mac-m1-beginner/blob/main/README.md`


    ❯ ls -lah /Users/<user> | grep .fly

        drwx------   11 <user>  staff   352B Mar 11 11:41 .fly


    ❯ killall flyctl
    
    
    ❯ rm -rf /usr/local/bin/fly/.fly


    ❯ sudo mv /Users/powercommerce/.fly /usr/local/bin/fly

        Password:


    ❯ sudo chmod -R 0700 /usr/local/bin/fly


    ❯ ls -lah /usr/local/bin | grep fly

        drwx------   5 powercommerce  staff   160B Mar 11 12:45 fly


    ❯ flyctl auth login

        Opening https://fly.io/app/auth/cli/0536cd82edce9a492c4dd7be56c13ab0 ...

        Waiting for session... Done
        successfully logged in as dp20bp@gmail.com


check and watch for updates on the fly.io console dashboard

<p align="center">
    <img src="./gambar-petunjuk/ss_dashboard_fly.io-1.png" alt="ss_dashboard_fly.io-1" style="display: block; margin: 0 auto;">
</p>


### deploy Apps :


    ❯ flyctl deploy

        ==> Verifying app config
        Validating /Users/powercommerce/Documents/test/from-github-all/python_fastapi/fly.toml
        ✓ Configuration is valid
        --> Verified app config
        ==> Building image
        Remote builder fly-builder-throbbing-shadow-8193 ready
        Remote builder fly-builder-throbbing-shadow-8193 ready
        ==> Building image with Docker
        --> docker host: 20.10.12 linux x86_64
        [+] Building 2.1s (11/11) FINISHED                                                                                                                                                                                                   
        => [internal] load build definition from Dockerfile                                                                           0.1s
        => => transferring dockerfile: 260B                                                                                           0.1s
        => [internal] load .dockerignore                                                                                              0.1s
        => => transferring context: 2B                                                                                                0.1s
        => [internal] load metadata for docker.io/library/python:3.8                                                                  1.6s
        => [1/6] FROM docker.io/library/python:3.8@sha256:12266a9bc0318a9e0131561fc98d53b75325a3c2abd62aebc8302e3beb503b05            0.0s
        => [internal] load build context                                                                                              0.3s
        => => transferring context: 283.21kB                                                                                          0.3s
        => CACHED [2/6] RUN useradd -ms /bin/bash user                                                                                0.0s
        => CACHED [3/6] WORKDIR /home/user                                                                                            0.0s
        => CACHED [4/6] COPY requirements.txt .                                                                                       0.0s
        => CACHED [5/6] RUN pip install -r requirements.txt && rm requirements.txt                                                    0.0s
        => [6/6] COPY . .                                                                                                             0.0s
        => exporting to image                                                                                                         0.0s
        => => exporting layers                                                                                                        0.0s
        => => writing image sha256:cb68045d461067dd128020795a27e28641e11067d2e4990f8e865d67d83e369d                                   0.0s
        => => naming to registry.fly.io/damvfastapitest:deployment-01HRPCJ5K760CJY1J4TACM39TY                                         0.0s
        --> Building image done
        ==> Pushing image to fly
        The push refers to repository [registry.fly.io/damvfastapitest]
        8dc4eda9fb96: Pushed 
        1b963ad31a1b: Pushed 
        abd4a0c45074: Pushed 
        5f70bf18a086: Pushed 
        4d281ae3d48f: Pushed 
        6e751b5b0bee: Pushed 
        126cdbcad241: Pushed 
        01589a17de95: Pushed 
        84f540ade319: Pushed 
        9fe4e8a1862c: Pushed 
        909275a3eaaa: Pushed 
        f3f47b3309ca: Pushed 
        1a5fc1184c48: Pushed 
        deployment-01HRPCJ5K760CJY1J4TACM39TY: digest: sha256:136a394ec3fd9dfa685a451728d4e848db6c8226f6fc2986467644c1a122ead2 size: 3050
        --> Pushing image done
        image: registry.fly.io/damvfastapitest:deployment-01HRPCJ5K760CJY1J4TACM39TY
        image size: 1.1 GB

        Watch your deployment at https://fly.io/apps/damvfastapitest/monitoring

        Provisioning ips for damvfastapitest
        Dedicated ipv6: 2a09:8280:1::2d:8b1b:0
        Shared ipv4: 66.241.125.214
        Add a dedicated ipv4 with: fly ips allocate-v4

        This deployment will:
        * create 2 "app" machines

        No machines in group app, launching a new machine
        Creating a second machine to increase service availability
        Finished launching new machines
        -------
        ✔ Machine 3287119f940285 [app] update finished: success

        -------
        Checking DNS configuration for damvfastapitest.fly.dev

        Visit your newly deployed app at https://damvfastapitest.fly.dev/


### check

    ❯ curl -X GET https://damvfastapitest.fly.dev

        "How are you doing ;-)!"%


    ❯ flyctl status

        App
        Name     = damvfastapitest                                        
        Owner    = personal                                               
        Hostname = damvfastapitest.fly.dev                                
        Image    = damvfastapitest:deployment-01HRPCJ5K760CJY1J4TACM39TY  

        Machines
        PROCESS ID              VERSION REGION  STATE   ROLE    CHECKS                  LAST UPDATED         
        app     3287119f940285  1       sin     started         1 total, 1 passing      2024-03-11T09:14:49Z
        app     6e82330f512287  1       sin     started         1 total, 1 passing      2024-03-11T09:14:26Z


    ❯ flyctl ips list

        VERSION IP                      TYPE                    REGION  CREATED AT       
        v6      2a09:8280:1::2d:8b1b:0  public (dedicated)      global  2h35m ago       
        v4      66.241.125.214          public (shared)                 Jan 1 0001 00:00

        Learn more about Fly.io public, private, shared and dedicated IP addresses in our docs: https://fly.io/docs/reference/services/#ip-addresses

    ❯ flyctl services list

        Services
        PROTOCOL        PORTS           HANDLERS        FORCE HTTPS     PROCESS GROUP   REGIONS MACHINES 
        TCP             80 => 10000     [HTTP]          True            app             sin     2       
        TCP             443 => 10000    [TLS,HTTP]      False           app             sin     2  


### open :

    ❯ flyctl open

        Command "open" is deprecated, use `fly apps open` instead
        opening https://damvfastapitest.fly.dev/ ...







# Install 

    ❯ curl -L https://fly.io/install.sh | sh

        % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                        Dload  Upload   Total   Spent    Left  Speed
        100  1735    0  1735    0     0   2829      0 --:--:-- --:--:-- --:--:--  2844
        ######################################################################## 100.0%
        set update channel to shell
        flyctl was installed successfully to /Users/powercommerce/.fly/bin/flyctl
        Manually add the directory to your $HOME/.zshrc (or similar)
        export FLYCTL_INSTALL="/Users/powercommerce/.fly"
        export PATH="$FLYCTL_INSTALL/bin:$PATH"
        Run '/Users/powercommerce/.fly/bin/flyctl --help' to get started



    ❯ ls -lah | grep .fly

        drwxr-xr-x    9 powercommerce  staff   288B Mar 11 16:06 .fly


    ❯ sudo mv .fly /usr/local/bin/fly

        Password:


    ❯ ls -lah /usr/local/bin | grep fly

        drwxr-xr-x   9 powercommerce  staff   288B Mar 11 16:06 fly


    ❯ sudo chmod -R 0700 /usr/local/bin/fly


    ❯ ls -lah /usr/local/bin | grep fly

        drwx------   9 powercommerce  staff   288B Mar 11 16:06 fly


    ❯ flyctl auth login

        Opening https://fly.io/app/auth/cli/06adefcf37dc25ca5fd4bb27a2cceaa6 ...

        Waiting for session... Done
        successfully logged in as dp20bp@gmail.com


    ❯ flyctl version

        flyctl v0.2.15 darwin/arm64 Commit: 846630217aff135b32ec0d6a018cf6bdde0f1762 BuildDate: 2024-03-10T09:52:28Z