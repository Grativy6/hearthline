# Hearthline toolkit installation

Hearthline is a public, model-neutral MCP toolkit. The default public profile
loads the mechanisms and maintained foundation only; it does not load Hearthline
lore, private memories, Moltbook material, or a model.

## Source installation

The maintained foundation and the Book of Peaches are currently installed from
their source repositories because these build artifacts are not published to a
package registry. Install them in dependency order:

```powershell
python -m pip install "cryptography==50.0.1" "mcp==1.28.0"
git clone https://github.com/Grativy6/book-of-peaches.git book-of-peaches
git -C book-of-peaches checkout c91ab35dcb6b594f91d59ebe08d45cad005d2c04
python -m pip install ./book-of-peaches
git clone https://github.com/Grativy6/seedpea-mcp-adapter.git seedpea-mcp-adapter
git -C seedpea-mcp-adapter checkout 45eb52243770f42cebe3e0c3afe096a271b86f98
python -m pip install ./seedpea-mcp-adapter/packages/foundation
python -m pip install .
```

The public server can then be started with:

```powershell
hearthline-mcp
```

The server uses the `public` profile by default. A host may supply an explicit
store root and namespace through `HEARTHLINE_STORE_ROOT` and
`HEARTHLINE_STORE_NAMESPACE`. These settings select storage; they do not grant
authority or permit external effects.

## Local wheelhouse installation

For an offline local build, install the wheels from the verified wheelhouse in
the same order:

```powershell
python -m pip install --no-index --find-links "<wheelhouse>" "peaches-book==0.1.0"
python -m pip install --no-index --find-links "<wheelhouse>" "seedpea-foundation==0.1.0"
python -m pip install --no-index --find-links "<wheelhouse>" "hearthline-toolkit==0.1.0"
```

Install the MCP runtime dependencies from the same wheelhouse before starting
the server. The build record identifies the exact versions and hashes used for
the verified snapshot.

## Scope

The toolkit records bounded context, continuity, provenance, and review data.
It does not create permission, authorization, consent, standing, truth, or
institutional approval. Heartbeats and TETHER records preserve recoverable
state; they do not renew authority or keep work alive by themselves.
