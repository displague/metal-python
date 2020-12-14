// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// FindBgpConfigByProjectReader is a Reader for the FindBgpConfigByProject structure.
type FindBgpConfigByProjectReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindBgpConfigByProjectReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindBgpConfigByProjectOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindBgpConfigByProjectUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindBgpConfigByProjectForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindBgpConfigByProjectNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindBgpConfigByProjectOK creates a FindBgpConfigByProjectOK with default headers values
func NewFindBgpConfigByProjectOK() *FindBgpConfigByProjectOK {
	return &FindBgpConfigByProjectOK{}
}

/*FindBgpConfigByProjectOK handles this case with default header values.

ok

When BGP configuration is not enabled empty structure is returned.
When BGP configuration is disabled after being enabled BGP configuration data is returned with status disabled.

*/
type FindBgpConfigByProjectOK struct {
	Payload *models.BgpConfig
}

func (o *FindBgpConfigByProjectOK) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/bgp-config][%d] findBgpConfigByProjectOK  %+v", 200, o.Payload)
}

func (o *FindBgpConfigByProjectOK) GetPayload() *models.BgpConfig {
	return o.Payload
}

func (o *FindBgpConfigByProjectOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.BgpConfig)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindBgpConfigByProjectUnauthorized creates a FindBgpConfigByProjectUnauthorized with default headers values
func NewFindBgpConfigByProjectUnauthorized() *FindBgpConfigByProjectUnauthorized {
	return &FindBgpConfigByProjectUnauthorized{}
}

/*FindBgpConfigByProjectUnauthorized handles this case with default header values.

unauthorized
*/
type FindBgpConfigByProjectUnauthorized struct {
}

func (o *FindBgpConfigByProjectUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/bgp-config][%d] findBgpConfigByProjectUnauthorized ", 401)
}

func (o *FindBgpConfigByProjectUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindBgpConfigByProjectForbidden creates a FindBgpConfigByProjectForbidden with default headers values
func NewFindBgpConfigByProjectForbidden() *FindBgpConfigByProjectForbidden {
	return &FindBgpConfigByProjectForbidden{}
}

/*FindBgpConfigByProjectForbidden handles this case with default header values.

forbidden
*/
type FindBgpConfigByProjectForbidden struct {
}

func (o *FindBgpConfigByProjectForbidden) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/bgp-config][%d] findBgpConfigByProjectForbidden ", 403)
}

func (o *FindBgpConfigByProjectForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindBgpConfigByProjectNotFound creates a FindBgpConfigByProjectNotFound with default headers values
func NewFindBgpConfigByProjectNotFound() *FindBgpConfigByProjectNotFound {
	return &FindBgpConfigByProjectNotFound{}
}

/*FindBgpConfigByProjectNotFound handles this case with default header values.

not found

The project was not found.

*/
type FindBgpConfigByProjectNotFound struct {
}

func (o *FindBgpConfigByProjectNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/bgp-config][%d] findBgpConfigByProjectNotFound ", 404)
}

func (o *FindBgpConfigByProjectNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
