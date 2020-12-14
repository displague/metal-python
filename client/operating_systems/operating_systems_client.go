// Code generated by go-swagger; DO NOT EDIT.

package operating_systems

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// New creates a new operating systems API client.
func New(transport runtime.ClientTransport, formats strfmt.Registry) ClientService {
	return &Client{transport: transport, formats: formats}
}

/*
Client for operating systems API
*/
type Client struct {
	transport runtime.ClientTransport
	formats   strfmt.Registry
}

// ClientService is the interface for Client methods
type ClientService interface {
	FindOperatingSystems(params *FindOperatingSystemsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOperatingSystemsOK, error)

	FindOperatingSystemsByOrganization(params *FindOperatingSystemsByOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*FindOperatingSystemsByOrganizationOK, error)

	SetTransport(transport runtime.ClientTransport)
}

/*
  FindOperatingSystems retrieves all operating systems

  Provides a listing of available operating systems to provision your new device with.
*/
func (a *Client) FindOperatingSystems(params *FindOperatingSystemsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOperatingSystemsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOperatingSystemsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOperatingSystems",
		Method:             "GET",
		PathPattern:        "/operating-systems",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOperatingSystemsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOperatingSystemsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOperatingSystems: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOperatingSystemsByOrganization retrieves all operating systems visible by the organization

  Returns a listing of available operating systems for the given organization
*/
func (a *Client) FindOperatingSystemsByOrganization(params *FindOperatingSystemsByOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*FindOperatingSystemsByOrganizationOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOperatingSystemsByOrganizationParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOperatingSystemsByOrganization",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/operating-systems",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOperatingSystemsByOrganizationReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOperatingSystemsByOrganizationOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOperatingSystemsByOrganization: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

// SetTransport changes the transport on the client
func (a *Client) SetTransport(transport runtime.ClientTransport) {
	a.transport = transport
}
