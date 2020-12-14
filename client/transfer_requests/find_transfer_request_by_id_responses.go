// Code generated by go-swagger; DO NOT EDIT.

package transfer_requests

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// FindTransferRequestByIDReader is a Reader for the FindTransferRequestByID structure.
type FindTransferRequestByIDReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindTransferRequestByIDReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindTransferRequestByIDOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindTransferRequestByIDUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindTransferRequestByIDForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindTransferRequestByIDNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindTransferRequestByIDOK creates a FindTransferRequestByIDOK with default headers values
func NewFindTransferRequestByIDOK() *FindTransferRequestByIDOK {
	return &FindTransferRequestByIDOK{}
}

/*FindTransferRequestByIDOK handles this case with default header values.

ok
*/
type FindTransferRequestByIDOK struct {
	Payload *models.TransferRequest
}

func (o *FindTransferRequestByIDOK) Error() string {
	return fmt.Sprintf("[GET /transfers/{id}][%d] findTransferRequestByIdOK  %+v", 200, o.Payload)
}

func (o *FindTransferRequestByIDOK) GetPayload() *models.TransferRequest {
	return o.Payload
}

func (o *FindTransferRequestByIDOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.TransferRequest)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindTransferRequestByIDUnauthorized creates a FindTransferRequestByIDUnauthorized with default headers values
func NewFindTransferRequestByIDUnauthorized() *FindTransferRequestByIDUnauthorized {
	return &FindTransferRequestByIDUnauthorized{}
}

/*FindTransferRequestByIDUnauthorized handles this case with default header values.

unauthorized
*/
type FindTransferRequestByIDUnauthorized struct {
}

func (o *FindTransferRequestByIDUnauthorized) Error() string {
	return fmt.Sprintf("[GET /transfers/{id}][%d] findTransferRequestByIdUnauthorized ", 401)
}

func (o *FindTransferRequestByIDUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindTransferRequestByIDForbidden creates a FindTransferRequestByIDForbidden with default headers values
func NewFindTransferRequestByIDForbidden() *FindTransferRequestByIDForbidden {
	return &FindTransferRequestByIDForbidden{}
}

/*FindTransferRequestByIDForbidden handles this case with default header values.

forbidden
*/
type FindTransferRequestByIDForbidden struct {
}

func (o *FindTransferRequestByIDForbidden) Error() string {
	return fmt.Sprintf("[GET /transfers/{id}][%d] findTransferRequestByIdForbidden ", 403)
}

func (o *FindTransferRequestByIDForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindTransferRequestByIDNotFound creates a FindTransferRequestByIDNotFound with default headers values
func NewFindTransferRequestByIDNotFound() *FindTransferRequestByIDNotFound {
	return &FindTransferRequestByIDNotFound{}
}

/*FindTransferRequestByIDNotFound handles this case with default header values.

not found
*/
type FindTransferRequestByIDNotFound struct {
}

func (o *FindTransferRequestByIDNotFound) Error() string {
	return fmt.Sprintf("[GET /transfers/{id}][%d] findTransferRequestByIdNotFound ", 404)
}

func (o *FindTransferRequestByIDNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
