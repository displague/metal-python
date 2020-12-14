// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// New creates a new devices API client.
func New(transport runtime.ClientTransport, formats strfmt.Registry) ClientService {
	return &Client{transport: transport, formats: formats}
}

/*
Client for devices API
*/
type Client struct {
	transport runtime.ClientTransport
	formats   strfmt.Registry
}

// ClientService is the interface for Client methods
type ClientService interface {
	CreateBgpSession(params *CreateBgpSessionParams, authInfo runtime.ClientAuthInfoWriter) (*CreateBgpSessionOK, *CreateBgpSessionCreated, error)

	CreateDeviceBatch(params *CreateDeviceBatchParams, authInfo runtime.ClientAuthInfoWriter) (*CreateDeviceBatchCreated, error)

	CreateIPAssignment(params *CreateIPAssignmentParams, authInfo runtime.ClientAuthInfoWriter) (*CreateIPAssignmentCreated, error)

	DeleteDevice(params *DeleteDeviceParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteDeviceNoContent, error)

	FindBgpSessions(params *FindBgpSessionsParams, authInfo runtime.ClientAuthInfoWriter) (*FindBgpSessionsOK, error)

	FindDeviceByID(params *FindDeviceByIDParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceByIDOK, error)

	FindDeviceCustomdata(params *FindDeviceCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceCustomdataOK, error)

	FindDeviceUsages(params *FindDeviceUsagesParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceUsagesOK, error)

	FindIPAssignmentCustomdata(params *FindIPAssignmentCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindIPAssignmentCustomdataOK, error)

	FindIPAssignments(params *FindIPAssignmentsParams, authInfo runtime.ClientAuthInfoWriter) (*FindIPAssignmentsOK, error)

	FindInstanceBandwidth(params *FindInstanceBandwidthParams, authInfo runtime.ClientAuthInfoWriter) (*FindInstanceBandwidthOK, error)

	FindProjectUsage(params *FindProjectUsageParams, authInfo runtime.ClientAuthInfoWriter) (*FindProjectUsageOK, error)

	FindTraffic(params *FindTrafficParams, authInfo runtime.ClientAuthInfoWriter) (*FindTrafficOK, error)

	GetBgpNeighborData(params *GetBgpNeighborDataParams, authInfo runtime.ClientAuthInfoWriter) (*GetBgpNeighborDataOK, error)

	PerformAction(params *PerformActionParams, authInfo runtime.ClientAuthInfoWriter) (*PerformActionAccepted, error)

	UpdateDevice(params *UpdateDeviceParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateDeviceOK, error)

	SetTransport(transport runtime.ClientTransport)
}

/*
  CreateBgpSession creates a b g p session

  Creates a BGP session.
*/
func (a *Client) CreateBgpSession(params *CreateBgpSessionParams, authInfo runtime.ClientAuthInfoWriter) (*CreateBgpSessionOK, *CreateBgpSessionCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateBgpSessionParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createBgpSession",
		Method:             "POST",
		PathPattern:        "/devices/{id}/bgp/sessions",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreateBgpSessionReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *CreateBgpSessionOK:
		return value, nil, nil
	case *CreateBgpSessionCreated:
		return nil, value, nil
	}
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for devices: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  CreateDeviceBatch creates a devices batch

  Creates new devices in batch and provisions them in our datacenter.

Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.

The features attribute allows you to optionally specify what features your server should have.

For example, if you require a server with a TPM chip, you may specify `{ "features": { "tpm": "required" } }` (or `{ "features": ["tpm"] }` in shorthand).

The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).

The request will not fail if we have no servers with that feature in our inventory.

The facilities attribute specifies in what datacenter you wish to create the device.

You can either specify a single facility `{ "facility": "f1" }` , or you can instruct to create the device in the best available datacenter `{ "facility": "any" }`. Additionally it is possible to set a prioritized location selection.

For example `{ "facility": ["f3", "f2", "any"] }` will try to assign to the facility f3, if there are no available f2, and so on. If "any" is not specified for "facility", the request will fail unless it can assign in the selected locations.

With `{ "facility": "any" }` you have the option to diversify to indicate how many facilities you are willing to be spread across. For this purpose use parameter: `facility_diversity_level = N`.

For example:

`{ "facilities": ["sjc1", "ewr1", "any"] ,  "facility_diversity_level" = 1, "quantity" = 10 }` will assign 10 devices into the same facility, trying first in "sjc1", and if there aren’t available, it will try in  "ewr1", otherwise any other.

The `ip_addresses` attribute will allow you to specify the addresses you want created with your device.

To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if `{ "ip_addresses": [{ "address_family": 4, "public": true }, { "address_family": 4, "public": false }, { "address_family": 6, "public": true }] }` was sent.

The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.

For example, to only configure your server with a private IPv4 address, you can send `{ "ip_addresses": [{ "address_family": 4, "public": false }] }`.

Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.

For example, `{ "ip_addresses": [..., {"address_family": 4, "public": true, "ip_reservations": ["uuid1", "uuid2"]}] }`

To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy.
*/
func (a *Client) CreateDeviceBatch(params *CreateDeviceBatchParams, authInfo runtime.ClientAuthInfoWriter) (*CreateDeviceBatchCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateDeviceBatchParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createDeviceBatch",
		Method:             "POST",
		PathPattern:        "/projects/{id}/devices/batch",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreateDeviceBatchReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*CreateDeviceBatchCreated)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for createDeviceBatch: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  CreateIPAssignment creates a ip assignment

  Creates an ip assignment for a device.
*/
func (a *Client) CreateIPAssignment(params *CreateIPAssignmentParams, authInfo runtime.ClientAuthInfoWriter) (*CreateIPAssignmentCreated, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateIPAssignmentParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "createIPAssignment",
		Method:             "POST",
		PathPattern:        "/devices/{id}/ips",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &CreateIPAssignmentReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*CreateIPAssignmentCreated)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for createIPAssignment: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  DeleteDevice deletes the device

  Deletes a device and deprovisions it in our datacenter.
*/
func (a *Client) DeleteDevice(params *DeleteDeviceParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteDeviceNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewDeleteDeviceParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "deleteDevice",
		Method:             "DELETE",
		PathPattern:        "/devices/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &DeleteDeviceReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*DeleteDeviceNoContent)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for deleteDevice: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindBgpSessions retrieves all b g p sessions

  Provides a listing of available BGP sessions for the device.
*/
func (a *Client) FindBgpSessions(params *FindBgpSessionsParams, authInfo runtime.ClientAuthInfoWriter) (*FindBgpSessionsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindBgpSessionsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findBgpSessions",
		Method:             "GET",
		PathPattern:        "/devices/{id}/bgp/sessions",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindBgpSessionsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindBgpSessionsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findBgpSessions: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindDeviceByID retrieves a device

  Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.
                         State value can be one of: active inactive queued or provisioning
*/
func (a *Client) FindDeviceByID(params *FindDeviceByIDParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceByIDOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindDeviceByIDParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findDeviceById",
		Method:             "GET",
		PathPattern:        "/devices/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindDeviceByIDReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindDeviceByIDOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findDeviceById: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindDeviceCustomdata retrieves the custom metadata of an instance

  Provides the custom metadata stored for this instance in json format
*/
func (a *Client) FindDeviceCustomdata(params *FindDeviceCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceCustomdataOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindDeviceCustomdataParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findDeviceCustomdata",
		Method:             "GET",
		PathPattern:        "/devices/{id}/customdata",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindDeviceCustomdataReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindDeviceCustomdataOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findDeviceCustomdata: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindDeviceUsages retrieves all usages for device

  Returns all usages for a device.
*/
func (a *Client) FindDeviceUsages(params *FindDeviceUsagesParams, authInfo runtime.ClientAuthInfoWriter) (*FindDeviceUsagesOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindDeviceUsagesParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findDeviceUsages",
		Method:             "GET",
		PathPattern:        "/devices/{id}/usages",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindDeviceUsagesReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindDeviceUsagesOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findDeviceUsages: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindIPAssignmentCustomdata retrieves the custom metadata of an IP assignment

  Provides the custom metadata stored for this IP Assignment in json format
*/
func (a *Client) FindIPAssignmentCustomdata(params *FindIPAssignmentCustomdataParams, authInfo runtime.ClientAuthInfoWriter) (*FindIPAssignmentCustomdataOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindIPAssignmentCustomdataParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findIPAssignmentCustomdata",
		Method:             "GET",
		PathPattern:        "/devices/{instance_id}/ips/{id}/customdata",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindIPAssignmentCustomdataReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindIPAssignmentCustomdataOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findIPAssignmentCustomdata: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindIPAssignments retrieves all ip assignments

  Returns all ip assignments for a device.
*/
func (a *Client) FindIPAssignments(params *FindIPAssignmentsParams, authInfo runtime.ClientAuthInfoWriter) (*FindIPAssignmentsOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindIPAssignmentsParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findIPAssignments",
		Method:             "GET",
		PathPattern:        "/devices/{id}/ips",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindIPAssignmentsReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindIPAssignmentsOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findIPAssignments: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindInstanceBandwidth retrieves an instance bandwidth

  Retrieve an instance bandwidth for a given period of time.
*/
func (a *Client) FindInstanceBandwidth(params *FindInstanceBandwidthParams, authInfo runtime.ClientAuthInfoWriter) (*FindInstanceBandwidthOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindInstanceBandwidthParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findInstanceBandwidth",
		Method:             "GET",
		PathPattern:        "/devices/{id}/bandwidth",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindInstanceBandwidthReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindInstanceBandwidthOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findInstanceBandwidth: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindProjectUsage retrieves all usages for project

  Returns all usages for a project.
*/
func (a *Client) FindProjectUsage(params *FindProjectUsageParams, authInfo runtime.ClientAuthInfoWriter) (*FindProjectUsageOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindProjectUsageParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findProjectUsage",
		Method:             "GET",
		PathPattern:        "/projects/{id}/usages",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindProjectUsageReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindProjectUsageOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findProjectUsage: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  FindTraffic retrieves device traffic

  Returns traffic for a specific device.
*/
func (a *Client) FindTraffic(params *FindTrafficParams, authInfo runtime.ClientAuthInfoWriter) (*FindTrafficOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewFindTrafficParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "findTraffic",
		Method:             "GET",
		PathPattern:        "/devices/{id}/traffic",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &FindTrafficReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*FindTrafficOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for findTraffic: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  GetBgpNeighborData retrieves b g p neighbor data for this device

  Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.
*/
func (a *Client) GetBgpNeighborData(params *GetBgpNeighborDataParams, authInfo runtime.ClientAuthInfoWriter) (*GetBgpNeighborDataOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewGetBgpNeighborDataParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "getBgpNeighborData",
		Method:             "GET",
		PathPattern:        "/devices/{id}/bgp/neighbors",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &GetBgpNeighborDataReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*GetBgpNeighborDataOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for getBgpNeighborData: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  PerformAction performs an action

  Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)
*/
func (a *Client) PerformAction(params *PerformActionParams, authInfo runtime.ClientAuthInfoWriter) (*PerformActionAccepted, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewPerformActionParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "performAction",
		Method:             "POST",
		PathPattern:        "/devices/{id}/actions",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &PerformActionReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*PerformActionAccepted)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for performAction: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

/*
  UpdateDevice updates the device

  Updates the device.
*/
func (a *Client) UpdateDevice(params *UpdateDeviceParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateDeviceOK, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewUpdateDeviceParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "updateDevice",
		Method:             "PUT",
		PathPattern:        "/devices/{id}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http"},
		Params:             params,
		Reader:             &UpdateDeviceReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, err
	}
	success, ok := result.(*UpdateDeviceOK)
	if ok {
		return success, nil
	}
	// unexpected success response
	// safeguard: normally, absent a default response, unknown success responses return an error above: so this is a codegen issue
	msg := fmt.Sprintf("unexpected success response for updateDevice: API contract not enforced by server. Client expected to get an error, but got: %T", result)
	panic(msg)
}

// SetTransport changes the transport on the client
func (a *Client) SetTransport(transport runtime.ClientTransport) {
	a.transport = transport
}
