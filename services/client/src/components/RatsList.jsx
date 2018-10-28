import React from 'react';

const RatsList = (props) => {
  return (
    <div>
      {
        props.rats.map((rat) => {
          return (
            <h4
              key={rat.id}
              className="box title is-4"
            >{ rat.color }
            <br />
             { rat.weight } grams
            </h4>
          )
        })
      }
    </div>
  )
};

export default RatsList;
