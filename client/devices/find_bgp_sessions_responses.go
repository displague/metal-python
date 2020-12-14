// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// FindBgpSessionsReader is a Reader for the FindBgpSessions structure.
type FindBgpSessionsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindBgpSessionsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindBgpSessionsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindBgpSessionsUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindBgpSessionsForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindBgpSessionsOK creates a FindBgpSessionsOK with default headers values
func NewFindBgpSessionsOK() *FindBgpSessionsOK {
	return &FindBgpSessionsOK{}
}

/*FindBgpSessionsOK handles this case with default header values.

ok
*/
type FindBgpSessionsOK struct {
	Payload *models.BgpSessionList
}

func (o *FindBgpSessionsOK) Error() string {
	return fmt.Sprintf("[GET /devices/{id}/bgp/sessions][%d] findBgpSessionsOK  %+v", 200, o.Payload)
}

func (o *FindBgpSessionsOK) GetPayload() *models.BgpSessionList {
	return o.Payload
}

func (o *FindBgpSessionsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.BgpSessionList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindBgpSessionsUnauthorized creates a FindBgpSessionsUnauthorized with default headers values
func NewFindBgpSessionsUnauthorized() *FindBgpSessionsUnauthorized {
	return &FindBgpSessionsUnauthorized{}
}

/*FindBgpSessionsUnauthorized handles this case with default header values.

unauthorized
*/
type FindBgpSessionsUnauthorized struct {
}

func (o *FindBgpSessionsUnauthorized) Error() string {
	return fmt.Sprintf("[GET /devices/{id}/bgp/sessions][%d] findBgpSessionsUnauthorized ", 401)
}

func (o *FindBgpSessionsUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindBgpSessionsForbidden creates a FindBgpSessionsForbidden with default headers values
func NewFindBgpSessionsForbidden() *FindBgpSessionsForbidden {
	return &FindBgpSessionsForbidden{}
}

/*FindBgpSessionsForbidden handles this case with default header values.

forbidden
*/
type FindBgpSessionsForbidden struct {
}

func (o *FindBgpSessionsForbidden) Error() string {
	return fmt.Sprintf("[GET /devices/{id}/bgp/sessions][%d] findBgpSessionsForbidden ", 403)
}

func (o *FindBgpSessionsForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
