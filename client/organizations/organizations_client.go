// Code generated by go-swagger; DO NOT EDIT.

package organizations

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// New creates a new organizations API client.
func New(transport runtime.ClientTransport, formats strfmt.Registry) ClientService {
	return &Client{transport: transport, formats: formats}
}

/*
Client for organizations API
*/
type Client struct {
	transport runtime.ClientTransport
	formats   strfmt.Registry
}

// ClientService is the interface for Client methods
type ClientService interface {
	CreateOrganization(params *CreateOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*CreateOrganizationCreated, error)

	CreateOrganizationProject(params *CreateOrganizationProjectParams, authInfo runtime.ClientAuthInfoWriter) (*CreateOrganizationProjectCreated, error)

	CreatePaymentMethod(params *CreatePaymentMethodParams, authInfo runtime.ClientAuthInfoWriter) (*CreatePaymentMethodCreated, error)

	DeleteOrganization(params *DeleteOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteOrganizationNoContent, error)

	FindOrganizationByID(params *FindOrganizationByIDParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationByIDOK, error)

	FindOrganizationCustomdata(params *FindOrganizationCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationCustomdataOK, error)

	FindOrganizationDevices(params *FindOrganizationDevicesParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationDevicesOK, error)

	FindOrganizationPaymentMethods(params *FindOrganizationPaymentMethodsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationPaymentMethodsOK, error)

	FindOrganizationProjects(params *FindOrganizationProjectsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationProjectsOK, error)

	FindOrganizationTransfers(params *FindOrganizationTransfersParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationTransfersOK, error)

	FindOrganizations(params *FindOrganizationsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationsOK, error)

	UpdateOrganization(params *UpdateOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateOrganizationOK, error)

	SetTransport(transport runtime.ClientTransport)
}

/*
  CreateOrganization creates an organization

  Creates an organization.
*/
func (a *Client) CreateOrganization(params *CreateOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*CreateOrganizationCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateOrganizationParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createOrganization",
		Method:             "POST",
		PathPattern:        "/organizations",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreateOrganizationReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*CreateOrganizationCreated)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for createOrganization: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  CreateOrganizationProject creates a project for the organization

  Creates a new project for the organization
*/
func (a *Client) CreateOrganizationProject(params *CreateOrganizationProjectParams, authInfo runtime.ClientAuthInfoWriter) (*CreateOrganizationProjectCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateOrganizationProjectParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createOrganizationProject",
		Method:             "POST",
		PathPattern:        "/organizations/{id}/projects",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreateOrganizationProjectReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*CreateOrganizationProjectCreated)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for createOrganizationProject: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  CreatePaymentMethod creates a payment method for the given organization

  Creates a payment method.
*/
func (a *Client) CreatePaymentMethod(params *CreatePaymentMethodParams, authInfo runtime.ClientAuthInfoWriter) (*CreatePaymentMethodCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreatePaymentMethodParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createPaymentMethod",
		Method:             "POST",
		PathPattern:        "/organizations/{id}/payment-methods",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreatePaymentMethodReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*CreatePaymentMethodCreated)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for createPaymentMethod: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  DeleteOrganization deletes the organization

  Deletes the organization.
*/
func (a *Client) DeleteOrganization(params *DeleteOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteOrganizationNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewDeleteOrganizationParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "deleteOrganization",
		Method:             "DELETE",
		PathPattern:        "/organizations/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &DeleteOrganizationReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*DeleteOrganizationNoContent)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for deleteOrganization: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationByID retrieves an organization s details

  Returns a single organization's details, if the user is authorized to view it.
*/
func (a *Client) FindOrganizationByID(params *FindOrganizationByIDParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationByIDOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationByIDParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationById",
		Method:             "GET",
		PathPattern:        "/organizations/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationByIDReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationByIDOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationById: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationCustomdata retrieves the custom metadata of an organization

  Provides the custom metadata stored for this organization in json format
*/
func (a *Client) FindOrganizationCustomdata(params *FindOrganizationCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationCustomdataOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationCustomdataParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationCustomdata",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/customdata",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationCustomdataReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationCustomdataOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationCustomdata: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationDevices retrieves all devices of an organization

  Provides a collection of devices for a given organization.
*/
func (a *Client) FindOrganizationDevices(params *FindOrganizationDevicesParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationDevicesOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationDevicesParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationDevices",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/devices",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationDevicesReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationDevicesOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationDevices: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationPaymentMethods retrieves all payment methods of an organization

  Returns all payment methods of an organization.
*/
func (a *Client) FindOrganizationPaymentMethods(params *FindOrganizationPaymentMethodsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationPaymentMethodsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationPaymentMethodsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationPaymentMethods",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/payment-methods",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationPaymentMethodsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationPaymentMethodsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationPaymentMethods: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationProjects retrieves all projects of an organization

  Returns a collection of projects that belong to the organization.
*/
func (a *Client) FindOrganizationProjects(params *FindOrganizationProjectsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationProjectsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationProjectsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationProjects",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/projects",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationProjectsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationProjectsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationProjects: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizationTransfers retrieves all project transfer requests from or to an organization

  Provides a collection of project transfer requests from or to the organization.
*/
func (a *Client) FindOrganizationTransfers(params *FindOrganizationTransfersParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationTransfersOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationTransfersParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizationTransfers",
		Method:             "GET",
		PathPattern:        "/organizations/{id}/transfers",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationTransfersReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationTransfersOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizationTransfers: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindOrganizations retrieves all organizations

  Returns a list of organizations that are accessible to the current user.
*/
func (a *Client) FindOrganizations(params *FindOrganizationsParams, authInfo runtime.ClientAuthInfoWriter) (*FindOrganizationsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindOrganizationsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findOrganizations",
		Method:             "GET",
		PathPattern:        "/organizations",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindOrganizationsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindOrganizationsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findOrganizations: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  UpdateOrganization updates the organization

  Updates the organization.
*/
func (a *Client) UpdateOrganization(params *UpdateOrganizationParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateOrganizationOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewUpdateOrganizationParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "updateOrganization",
		Method:             "PUT",
		PathPattern:        "/organizations/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &UpdateOrganizationReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*UpdateOrganizationOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for updateOrganization: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

// SetTransport changes the transport on the client
func (a *Client) SetTransport(transport runtime.ClientTransport) {
	a.transport = transport
}
