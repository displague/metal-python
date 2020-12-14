// Code generated by go-swagger; DO NOT EDIT.

package v_l_a_ns

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// GetVirtualNetworkReader is a Reader for the GetVirtualNetwork structure.
type GetVirtualNetworkReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *GetVirtualNetworkReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewGetVirtualNetworkOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewGetVirtualNetworkUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewGetVirtualNetworkForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewGetVirtualNetworkNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewGetVirtualNetworkUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewGetVirtualNetworkOK creates a GetVirtualNetworkOK with default headers values
func NewGetVirtualNetworkOK() *GetVirtualNetworkOK {
	return &GetVirtualNetworkOK{}
}

/*GetVirtualNetworkOK handles this case with default header values.

ok
*/
type GetVirtualNetworkOK struct {
	Payload *models.VirtualNetwork
}

func (o *GetVirtualNetworkOK) Error() string {
	return fmt.Sprintf("[GET /virtual-networks/{id}][%d] getVirtualNetworkOK  %+v", 200, o.Payload)
}

func (o *GetVirtualNetworkOK) GetPayload() *models.VirtualNetwork {
	return o.Payload
}

func (o *GetVirtualNetworkOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.VirtualNetwork)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewGetVirtualNetworkUnauthorized creates a GetVirtualNetworkUnauthorized with default headers values
func NewGetVirtualNetworkUnauthorized() *GetVirtualNetworkUnauthorized {
	return &GetVirtualNetworkUnauthorized{}
}

/*GetVirtualNetworkUnauthorized handles this case with default header values.

unauthorized
*/
type GetVirtualNetworkUnauthorized struct {
}

func (o *GetVirtualNetworkUnauthorized) Error() string {
	return fmt.Sprintf("[GET /virtual-networks/{id}][%d] getVirtualNetworkUnauthorized ", 401)
}

func (o *GetVirtualNetworkUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewGetVirtualNetworkForbidden creates a GetVirtualNetworkForbidden with default headers values
func NewGetVirtualNetworkForbidden() *GetVirtualNetworkForbidden {
	return &GetVirtualNetworkForbidden{}
}

/*GetVirtualNetworkForbidden handles this case with default header values.

forbidden
*/
type GetVirtualNetworkForbidden struct {
}

func (o *GetVirtualNetworkForbidden) Error() string {
	return fmt.Sprintf("[GET /virtual-networks/{id}][%d] getVirtualNetworkForbidden ", 403)
}

func (o *GetVirtualNetworkForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewGetVirtualNetworkNotFound creates a GetVirtualNetworkNotFound with default headers values
func NewGetVirtualNetworkNotFound() *GetVirtualNetworkNotFound {
	return &GetVirtualNetworkNotFound{}
}

/*GetVirtualNetworkNotFound handles this case with default header values.

not found
*/
type GetVirtualNetworkNotFound struct {
}

func (o *GetVirtualNetworkNotFound) Error() string {
	return fmt.Sprintf("[GET /virtual-networks/{id}][%d] getVirtualNetworkNotFound ", 404)
}

func (o *GetVirtualNetworkNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewGetVirtualNetworkUnprocessableEntity creates a GetVirtualNetworkUnprocessableEntity with default headers values
func NewGetVirtualNetworkUnprocessableEntity() *GetVirtualNetworkUnprocessableEntity {
	return &GetVirtualNetworkUnprocessableEntity{}
}

/*GetVirtualNetworkUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type GetVirtualNetworkUnprocessableEntity struct {
}

func (o *GetVirtualNetworkUnprocessableEntity) Error() string {
	return fmt.Sprintf("[GET /virtual-networks/{id}][%d] getVirtualNetworkUnprocessableEntity ", 422)
}

func (o *GetVirtualNetworkUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
