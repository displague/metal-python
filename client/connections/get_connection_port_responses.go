// Code generated by go-swagger; DO NOT EDIT.

package connections

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// GetConnectionPortReader is a Reader for the GetConnectionPort structure.
type GetConnectionPortReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *GetConnectionPortReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewGetConnectionPortOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewGetConnectionPortForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewGetConnectionPortNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewGetConnectionPortOK creates a GetConnectionPortOK with default headers values
func NewGetConnectionPortOK() *GetConnectionPortOK {
	return &GetConnectionPortOK{}
}

/*GetConnectionPortOK handles this case with default header values.

ok
*/
type GetConnectionPortOK struct {
	Payload *models.InterconnectionPort
}

func (o *GetConnectionPortOK) Error() string {
	return fmt.Sprintf("[GET /connections/{connection_id}/ports/{id}][%d] getConnectionPortOK  %+v", 200, o.Payload)
}

func (o *GetConnectionPortOK) GetPayload() *models.InterconnectionPort {
	return o.Payload
}

func (o *GetConnectionPortOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.InterconnectionPort)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewGetConnectionPortForbidden creates a GetConnectionPortForbidden with default headers values
func NewGetConnectionPortForbidden() *GetConnectionPortForbidden {
	return &GetConnectionPortForbidden{}
}

/*GetConnectionPortForbidden handles this case with default header values.

forbidden
*/
type GetConnectionPortForbidden struct {
}

func (o *GetConnectionPortForbidden) Error() string {
	return fmt.Sprintf("[GET /connections/{connection_id}/ports/{id}][%d] getConnectionPortForbidden ", 403)
}

func (o *GetConnectionPortForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewGetConnectionPortNotFound creates a GetConnectionPortNotFound with default headers values
func NewGetConnectionPortNotFound() *GetConnectionPortNotFound {
	return &GetConnectionPortNotFound{}
}

/*GetConnectionPortNotFound handles this case with default header values.

not found
*/
type GetConnectionPortNotFound struct {
}

func (o *GetConnectionPortNotFound) Error() string {
	return fmt.Sprintf("[GET /connections/{connection_id}/ports/{id}][%d] getConnectionPortNotFound ", 404)
}

func (o *GetConnectionPortNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
