# Golang client for Equinix Metal generated with go-swagger

This is experimental. Don't use it.

This repo contains Golang code generated from customized [equinix-metal.swagger.json](equinix-metal.swagger.json) from the Equinix Metal API from <https://api.equinix.com/metal/v1/api-docs>.

Contents:
- `Makefile` includes tasks to fetch the API spec, apply patches, and generate a client
- `equinix-metal.fetched.json` the latest fetched swagger spec
- `equinix-metal.patched.json` the latest patched swagger spec
- `patches/*.patch` patch files to apply against the Equinix Metal API spec
- `clients/` generated clients
- `types/` generated types
- `examples/` hand crafted examples to demonstrate usage


## Build

To build the client, run `make`.

## Examples

You can see usage of the generated code in the `examples` directory. In order to try, export `METAL_AUTH_TOKEN` token and execute the code, e.g.

```
$ METAL_AUTH_TOKEN=... go run examples/projects/projects.go
[...]
$ cd examples/plans; METAL_AUTH_TOKEN=... go run .
```

## Patches

Patches can be generated by modifying a prestine `equinix-metal.fetched.json` or `equinix-metal.patched.json` file and running:

```
git diff equinix-metal.fetched.json > patches/01-name-of-patch.patch
```

Run `make` and `git diff equinix-metal.patched.json` to verify that the changes have persisted corrected.

The `json` code is very similar in areas. It may be necessary to include more context lines in the patch to prevent the patch from applying to the wrong endpoint or model.

`git diff -U7`, or greater `-U` values can be used to ensure that the adjacent endpoint or model is referenced in the patch file. This will ensure that the patch has not drifted to another resource due to other changes.

## Generated code

The generated functions look like (project listing):

```go
FindProjects(params *FindProjectsParams, authInfo runtime.ClientAuthInfoWriter) (*FindProjectsOK, error)
```

.. where authInfo is used for HTTP auth (auth token to header in case of Equinix Metal) and params are sth like

```go
type FindProjectsParams struct {
    Include *string
    Page *int64
    PerPage *int64
    timeout    time.Duration
    Context    context.Context
    HTTPClient *http.Client
}
```

There's an `HTTPClient` in the params and the client can maybe used for isolated HTTP traffic logging.



## Notes

- authentication struct must be passed to every function. All the generated functions have authWriter as an argument. I'm not sure if it's possible to set the auth header globally so that all the func use it. And I'm not sure if it's possible to remove the authWrite from the generated code.
