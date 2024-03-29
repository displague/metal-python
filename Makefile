.PHONY: all gen patch fetch clean validate test

SPEC_URL:=https://api.equinix.com/metal/v1/api-docs
SPEC_FETCHED_FILE:=fetched.openapi.yaml
SPEC_PATCHED_FILE:=patched.openapi.yaml
IMAGE=openapitools/openapi-generator-cli
GIT_ORG=displague
GIT_REPO=metal-python
PACKAGE_NAME=metal
# python-flask python-legacy python python-aiohttp python-blueplanet
GENERATOR=python-legacy
CRI=$(shell which nerdctl > /dev/null && echo nerdctl || echo docker)
SWAGGER=${CRI} run --rm -v $(CURDIR):/local ${IMAGE}
# CONVERT="curl -q ${SPEC_URL} | python3 -c 'import sys, yaml, json; j=json.loads(sys.stdin.read()); print(yaml.safe_dump(j))'"
CONVERT=${CRI} run --rm -i mikefarah/yq -P
all: pull fetch patch clean gen

pull:
	${CRI} pull ${IMAGE}

fetch:
	curl -q ${SPEC_URL} | ${CONVERT} > ${SPEC_FETCHED_FILE}

patch:
	# patch is idempotent, always starting with the fetched
	# fetched file to create the patched file.
	cp ${SPEC_FETCHED_FILE} ${SPEC_PATCHED_FILE}
	ARGS="-o ${SPEC_PATCHED_FILE} ${SPEC_FETCHED_FILE}"; \
	for diff in $(shell find patches/${SPEC_FETCHED_FILE} -name \*.patch | sort -n); do \
		patch --no-backup-if-mismatch -N -t $$ARGS $$diff; \
		ARGS=${SPEC_PATCHED_FILE}; \
	done

clean:
	rm -rf metal docs test

validate:
	${SWAGGER} validate \
		--recommend \
		-i /local/${SPEC_PATCHED_FILE}

gen:
	${SWAGGER} generate -g ${GENERATOR} \
		--package-name ${PACKAGE_NAME} \
		--model-package types \
		--api-package models \
		--git-user-id ${GIT_ORG} \
		--git-repo-id ${GIT_REPO} \
		-o /local/ \
		-i /local/${SPEC_PATCHED_FILE}

test:
	tox
