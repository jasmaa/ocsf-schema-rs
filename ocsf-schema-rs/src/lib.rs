use typify::import_types;

use serde::{Deserialize, Serialize};

import_types!(schema = "../data/all.json", struct_builder = true);
