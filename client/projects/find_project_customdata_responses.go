// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// FindProjectCustomdataReader is a Reader for the FindProjectCustomdata structure.
type FindProjectCustomdataReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindProjectCustomdataReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindProjectCustomdataOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindProjectCustomdataUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindProjectCustomdataForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindProjectCustomdataNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindProjectCustomdataOK creates a FindProjectCustomdataOK with default headers values
func NewFindProjectCustomdataOK() *FindProjectCustomdataOK {
	return &FindProjectCustomdataOK{}
}

/*FindProjectCustomdataOK handles this case with default header values.

ok
*/
type FindProjectCustomdataOK struct {
}

func (o *FindProjectCustomdataOK) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/customdata][%d] findProjectCustomdataOK ", 200)
}

func (o *FindProjectCustomdataOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectCustomdataUnauthorized creates a FindProjectCustomdataUnauthorized with default headers values
func NewFindProjectCustomdataUnauthorized() *FindProjectCustomdataUnauthorized {
	return &FindProjectCustomdataUnauthorized{}
}

/*FindProjectCustomdataUnauthorized handles this case with default header values.

unauthorized
*/
type FindProjectCustomdataUnauthorized struct {
}

func (o *FindProjectCustomdataUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/customdata][%d] findProjectCustomdataUnauthorized ", 401)
}

func (o *FindProjectCustomdataUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectCustomdataForbidden creates a FindProjectCustomdataForbidden with default headers values
func NewFindProjectCustomdataForbidden() *FindProjectCustomdataForbidden {
	return &FindProjectCustomdataForbidden{}
}

/*FindProjectCustomdataForbidden handles this case with default header values.

forbidden
*/
type FindProjectCustomdataForbidden struct {
}

func (o *FindProjectCustomdataForbidden) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/customdata][%d] findProjectCustomdataForbidden ", 403)
}

func (o *FindProjectCustomdataForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectCustomdataNotFound creates a FindProjectCustomdataNotFound with default headers values
func NewFindProjectCustomdataNotFound() *FindProjectCustomdataNotFound {
	return &FindProjectCustomdataNotFound{}
}

/*FindProjectCustomdataNotFound handles this case with default header values.

not found
*/
type FindProjectCustomdataNotFound struct {
}

func (o *FindProjectCustomdataNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/customdata][%d] findProjectCustomdataNotFound ", 404)
}

func (o *FindProjectCustomdataNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
