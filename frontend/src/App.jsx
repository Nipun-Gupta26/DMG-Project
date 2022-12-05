import { useEffect, useState } from 'react';
import csvFile from './assets/review_tags.csv'
import { Select, Option, Button, Checkbox } from "@material-tailwind/react";
// import { getTags } from './services/api.js';

function App() {
  const [csvData, setCsvData] = useState([]);
  const [csvHeaders, setCsvHeaders] = useState([]);

  useEffect(() => {
    fetch(csvFile)
      .then(response => response.text())
      .then(text => {
        const rows = text.split('\n');
        const headers = rows[0].split(',');
        // remove last 2 columns
        setCsvHeaders(headers);
        const data = rows.slice(1).map(row => {
          if (row === '') {
            return null;
          }
          const tempValues = row.split(',"');
          // console.log(tempValues);
          const Name = tempValues[0];
          const tempValues2 = tempValues[1].split('",');
          const Address = tempValues2[0];
          const tempValues3 = tempValues2[1].split(',');
          const eachRow = {};
          headers.forEach((header, index) => {
            if (index === 0) {
              eachRow[header] = Name;
            }
            else if (index === 1) {
              eachRow[header] = Address;
            }
            else {
              eachRow[header] = tempValues3[index - 2];
            }
          });
          return eachRow;
        });
        setCsvData(data);
        // console.log(data);
      });
  }, []);

  const [tags, setTags] = useState([]);
  const apiUri = 'http://localhost:5000';
  useEffect(() => {
    const getTagsFromApi = async () => {
      const response = await fetch(`${apiUri}/colName`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const data = await response.json();
      setTags(data);
    }
    getTagsFromApi();
  }, []);


  const [price, setPrice] = useState('Low');
  const priceOptions = ['Low', 'Medium', 'High'];

  const setPriceFilter = (e) => {
    // console.log(e);
    setPrice(e);
    console.log(price);
  }

  const [rating, setRating] = useState('Low');
  const ratingOptions = ['Low', 'Medium', 'High'];

  const setRatingFilter = (e) => {
    // console.log(e);
    setRating(e);
    console.log(rating);
  }


  const getRecommendationsByPrice = async () => {
    // const body = {
    //   P: price,
    //   R: rating,
    // }
    // console.log(body);
    // const response = await fetch(`${apiUri}/priceIndex`, {
    //   method: 'POST',
    //   // crossDomain:true,
    //   // mode: 'no-cors',
    //   mode: 'cors',
    //   headers: {
    //     'Content-Type': 'application/json',
    //     'Access-Control-Allow-Origin': '*',
    //   },
    //   body: JSON.stringify(body),
    // });
    // console.log(response);
    // const data = await response.json();
    // console.log(data);
    const string = rating + " Rating " + "and " + price + " Cost";
    let newData = []
    console.log(string);
    csvData.forEach((row) => {
      // console.log(row['cluster_description'].localeCompare(string));
      if (row === null) {
        return;
      }
      if (row['cluster_description'] === string) {
        newData.push(row);
      }
    });
    console.log(newData);
    setCsvData(newData);

  }

  const [selectedTags, setSelectedTags] = useState([]);

  const updateTags = (e) => {
    console.log(e.target.value);
    if (selectedTags.includes(e.target.value)) {
      setSelectedTags(selectedTags.filter(tag => tag !== e.target.value));
    }
    else {
      setSelectedTags([...selectedTags, e.target.value]);
    }
    console.log(selectedTags);
  }

  const getRecommendationsByTags = () => {
    let newData = [];
    csvData.forEach((row) => {
      if (row === null) {
        return;
      }
      let flag = true;
      selectedTags.forEach((tag) => {
        if (row[tag] === 0) {
          flag = false;
        }
      });
      if (flag) {
        newData.push(row);
      }
    });
    console.log(newData);
    setCsvData(newData);
  }




  return (
    <div className="App">
      <div className="bg-white p-8 rounded-md w-full">
        <h1 className="text-2xl font-bold w-full text-center mb-10">Welcome to the recommender system</h1>
        <div className=" flex items-center justify-between pb-6">
          <div className="flex gap-4">
            <Select variant="outlined" label="Select Price" onChange={setPriceFilter}>
              {priceOptions.map((item, index) => (
                <Option key={index} value={item}>
                  {item}
                </Option>
              ))}
            </Select>
            <Select variant="outlined" label="Select Rating" onChange={setRatingFilter}>
              {ratingOptions.map((item, index) => (
                <Option key={index} value={item}>
                  {item}
                </Option>
              ))}
            </Select>
            <Select variant="outlined" label="Select Price" onChange={setPriceFilter}>
              {tags.map((item, index) => (
                <Checkbox key={index} value={item} label={item} onChange={updateTags} />
              ))}
            </Select>
          </div>
          <div className="flex items-center justify-between">

            <div className="lg:ml-40 ml-10 space-x-8">
              <Button color="lightBlue" buttonType="filled" size="regular" rounded={false} block={false} iconOnly={false} ripple="light" onClick={getRecommendationsByPrice}>
                Get Recommendations By Rate and price
              </Button>
            </div>
            <div className="lg:ml-40 ml-10 space-x-8">
              <Button color="lightBlue" buttonType="filled" size="regular" rounded={false} block={false} iconOnly={false} ripple="light" onClick={getRecommendationsByTags}>
                Get Recommendations By tags
              </Button>
            </div>
          </div>
        </div>
        <div>
          <div className="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
            <div className="inline-block min-w-full shadow rounded-lg overflow-hidden">
              <table className="min-w-full leading-normal">
                <thead className='sticky top-0'>
                  <tr>
                    {csvHeaders.map((header, index) => (
                      index < 5?
                      <th
                        key={header}
                        className="px-5 sticky top-0 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        {header}
                      </th>
                      : null
                    ))
                    }

                  </tr>
                </thead>
                <tbody>
                  {csvData && csvData.map((data, index) => (
                    <TableRow key={index} data={data} />
                  ))
                  }
                </tbody>
              </table>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

function TableRow(props) {
  const data = props.data;
  if (data === null) {
    return null;
  }
  const known = data['Known For'];
  return (
    <tr>
      {data && Object.keys(data).map((key, index) => (
        index < 5 ?
        <td key={index} className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
          <p className="text-gray-900 whitespace-no-wrap">
            {data[key]}
          </p>
        </td>
        :
        <></>
      ))
      }

    </tr>
  )
}

// const DropdownFilter = (data, value, onChange) => {
//   data = data.data
//   value = data.value
//   onChange = data.onChange
//   console.log(data);
//   const [value, setValue] = useState(data.value);
//   return (
//     <Select variant="outlined" label="Select Version">
//       {data.map((item, index) => (
//         <Option key={index} value={item}>
//           {item}
//         </Option>
//       ))}
//     </Select>
//   );
// }