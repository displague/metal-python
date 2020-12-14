// Code generated by go-swagger; DO NOT EDIT.

package facilities

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// New creates a new facilities API client.
func New(transport runtime.ClientTransport, formats strfmt.Registry) ClientService {
	return &Client{transport: transport, formats: formats}
}

/*
Client for facilities API
*/
type Client struct {
	transport runtime.ClientTransport
	formats   strfmt.Registry
}

// ClientService is the interface for Client methods
type ClientService interface {
	FindFacilities(params *FindFacilitiesParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesOK, error)

	FindFacilitiesByOrganization(params *FindFacilitiesByOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesByOrganizationOK, error)

	FindFacilitiesByProject(params *FindFacilitiesByProjectParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesByProjectOK, error)

	SetTransport(transport runtime.ClientTransport)
}

/*
  FindFacilities retrieves all facilities

  Provides a listing of available datacenters where you can provision Packet devices.
*/
func (a *Client) FindFacilities(params *FindFacilitiesParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindFacilitiesParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findFacilities",
		Method:             "GET",
		PathPattern:        "/facilities",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindFacilitiesReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindFacilitiesOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findFacilities: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindFacilitiesByOrganization retrieves all facilities visible by the organization

  Returns a listing of available datacenters for the given organization
*/
func (a *Client) FindFacilitiesByOrganization(params *FindFacilitiesByOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesByOrganizationOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindFacilitiesByOrganizationParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findFacilitiesByOrganization",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/facilities",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindFacilitiesByOrganizationReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindFacilitiesByOrganizationOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findFacilitiesByOrganization: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindFacilitiesByProject retrieves all facilities visible by the project

  Returns a listing of available datacenters for the given project
*/
func (a *Client) FindFacilitiesByProject(params *FindFacilitiesByProjectParams, authInfo runtime.ClientAuthInfoWriter) (*FindFacilitiesByProjectOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindFacilitiesByProjectParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findFacilitiesByProject",
		Method:             "GET",
		PathPattern:        "/projects/{id}/facilities",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindFacilitiesByProjectReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindFacilitiesByProjectOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findFacilitiesByProject: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

// SetTransport changes the transport on the client
func (a *Client) SetTransport(transport runtime.ClientTransport) {
	a.transport = transport
}
