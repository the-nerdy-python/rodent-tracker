import React from 'react';

const AddRat = (props) => {
  return (
    <form onSubmit={(event) => props.addRat(event)}>
      <div className="field">
        <input
          name="color"
          className="input is-large"
          type="text"
          placeholder="Enter a color"
          required
          value={props.color}
          onChange={props.handleChange}
        />
      </div>
      <div className="field">
        <input
          name="weight"
          className="input is-large"
          type="email"
          placeholder="Enter an weight in grams"
          required
          value={props.weight}
          onChange={props.handleChange}
        />
      </div>
      <input
        type="submit"
        className="button is-primary is-large is-fullwidth"
        value="Submit"
      />
    </form>
  )
};

export default AddRat;
